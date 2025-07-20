import asyncio
import aiohttp
from web3 import AsyncWeb3
from telebot import TeleBot
import config
import logging
from typing import Optional
import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
bot = TeleBot(config.TELEGRAM_TOKEN)


evm_web3_clients = {
    name: AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(details["url"]))
    for name, details in config.NETWORKS.items() if details["type"] == "evm"
}

# --- Функции для получения цен ---

async def get_gas_price_evm(network_name: str) -> Optional[float]:
    """Асинхронно получает цену газа для EVM-совместимой сети."""
    try:
        w3 = evm_web3_clients[network_name]
        gas_price_wei = await w3.eth.gas_price
        return round(gas_price_wei / 10**9, 3)
    except Exception as e:
        logging.error(f"Could not fetch gas price for {network_name}: {e}")
        return None

async def get_gas_price_starknet() -> Optional[float]:
    """Асинхронно получает цену газа для StarkNet одним запросом."""
    url = config.NETWORKS["STARKNET"]["url"]
    payload = {
        "jsonrpc": "2.0",
        "method": "starknet_getBlockWithTxHashes",
        "params": ["latest"],
        "id": 1
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=10) as response:
                response.raise_for_status()
                data = await response.json()
                price_in_wei_hex = data.get("result", {}).get("l1_gas_price", {}).get("price_in_wei")
                if price_in_wei_hex:
                    return round(int(price_in_wei_hex, 16) / 10**9, 3)
                logging.warning("L1 gas price not found in StarkNet response.")
                return None
    except Exception as e:
        logging.error(f"Could not fetch gas price for StarkNet: {e}")
        return None

# --- Вспомогательные функции ---

def get_gas_emoji(gas_price: Optional[float]) -> str:
    """Возвращает эмодзи в зависимости от цены на газ."""
    if gas_price is None:
        return "❓"
    if gas_price <= config.GAS_THRESHOLDS["ok"]:
        return "🟢"
    if gas_price <= config.GAS_THRESHOLDS["warn"]:
        return "🟠"
    return "🔴"

def format_final_message(network_prices: dict) -> str:
    """Собирает красивое итоговое сообщение из данных о ценах."""
    
    header = "📊  <b>G A S   M O N I T O R</b>  📊\n=====================\n"
    
    # Разделяем сети на рабочие и проблемные
    l1_networks = []
    l2_networks = []
    failed_networks = []

    # Определяем, какие сети L1, а какие L2 (можно вынести в конфиг)
    l1_list = ["ETH", "STARKNET"] 

    for name, price in network_prices.items():
        if price is not None:
            line = f"{get_gas_emoji(price)} {name}: <code>{price:.3f} Gwei</code>"
            if name in l1_list:
                l1_networks.append(line)
            else:
                l2_networks.append(line)
        else:
            line = f"❓ {name}: <i>Нет данных</i>"
            failed_networks.append(line)

    # Собираем блоки сообщения
    message_body = ""
    if l1_networks:
        message_body += "\n<b>L1 NETWORKS:</b>\n" + "\n".join(l1_networks) + "\n"
    
    if l2_networks:
        message_body += "\n<b>L2 NETWORKS:</b>\n" + "\n".join(l2_networks) + "\n"

    if failed_networks:
        message_body += "\n⚠️ <b>Проблемные сети:</b>\n" + "\n".join(failed_networks) + "\n"
        
    # Футер с точным временем
    current_time_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%d.%m.%Y %H:%M:%S UTC")
    footer = f"=====================\n⏰ <code>{current_time_utc}</code>\n{config.FOOTER_TEXT}"

    return header + message_body + footer


async def send_telegram_message(message: str):
    """Отправляет сообщение в Telegram, не блокируя основной поток."""
    def _send():
        try:
            # Убедитесь, что PHOTO_PATH ведет к подготовленному квадратному изображению
            with open(config.PHOTO_PATH, 'rb') as photo_file:
                bot.send_photo(
                    chat_id=config.CHAT_ID,
                    photo=photo_file,
                    caption=message,
                    parse_mode='HTML'
                )
            logging.info("Message sent successfully.")
        except Exception as e:
            logging.error(f"Failed to send Telegram message: {e}")

    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, _send)


# --- Основной цикл (ЗАМЕНИТЬ ЧАСТЬ ЛОГИКИ СБОРКИ СООБЩЕНИЯ) ---

async def main():
    last_sent_time = 0
    
    while True:
        current_loop_time = asyncio.get_running_loop().time()

        # ... (код для сбора задач и выполнения await asyncio.gather(...) остается тем же) ...
        tasks = []
        for name, details in config.NETWORKS.items():
            if details["type"] == "evm":
                tasks.append(get_gas_price_evm(name))
            elif details["type"] == "starknet":
                tasks.append(get_gas_price_starknet())

        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Обрабатываем возможные исключения от gather
        processed_results = [res if not isinstance(res, Exception) else None for res in results]
        network_prices = dict(zip(config.NETWORKS.keys(), processed_results))
        
        # Формируем и отправляем сообщение, если прошло достаточно времени
        if current_loop_time - last_sent_time >= config.SEND_INTERVAL_SECONDS:
            
            # Используем нашу новую красивую функцию форматирования
            final_message = format_final_message(network_prices)
            
            await send_telegram_message(final_message)
            last_sent_time = current_loop_time

        await asyncio.sleep(config.CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user.")
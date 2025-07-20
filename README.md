# ⛽ Telegram Gas Price Tracker Bot

<div align="center">

![Gas Tracker Bot](https://img.shields.io/badge/Gas-Tracker-blue?style=for-the-badge&logo=telegram)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
[![Telegram Channel](https://img.shields.io/badge/📢-Telegram_Channel-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/gastastion)

### 🌐 Language / Язык
[![EN](https://img.shields.io/badge/🇺🇸-English-blue?style=for-the-badge)](#-english-version)
[![RU](https://img.shields.io/badge/🇷🇺-Русский-red?style=for-the-badge)](#-русская-версия)

</div>

---

# 🇺🇸 English Version

<div align="center">

*Simple and efficient Python bot for monitoring gas prices across multiple blockchain networks*

**📢 Join our Telegram Channel: [Gas Station](https://t.me/gastastion)** 

[📋 Features](#-features) • [🚀 Quick Start](#-quick-start) • [🐳 Docker](#-docker-deployment) • [⚙️ Configuration](#️-configuration)

</div>

---

## 📊 Supported Networks

<div align="center">

| Network | Status | RPC Provider |
|---------|--------|--------------|
| 🔷 **Ethereum** | ✅ Active | Alchemy |
| 💥 **Blast** | ✅ Active | Ankr |
| 📜 **Scroll** | ✅ Active | Ankr |  
| 🟢 **Linea** | ✅ Active | Alchemy |
| 🔵 **Base** | ✅ Active | Alchemy |
| ⭐ **Starknet** | ✅ Active | Alchemy |

</div>

## ✨ Features

<table>
<tr>
<td>

### 🌐 Multi-Network Monitoring
Tracks gas prices across 6 major blockchain networks simultaneously

</td>
<td>

### ⚡ Asynchronous Architecture  
Uses `asyncio` for parallel requests and high performance

</td>
</tr>
<tr>
<td>

### 💎 Professional Formatting
Beautifully formatted messages with emojis, network grouping and timestamps

</td>
<td>

### 🛠️ Flexible Configuration
All parameters easily configurable through `.env` file without code changes

</td>
</tr>
<tr>
<td>

### 🐳 Docker Ready
Fully prepared for container deployment on any server

</td>
<td>

### 🎯 Smart Notifications
Configurable thresholds for high gas price warnings

</td>
</tr>
</table>

## 🚀 Quick Start

### 📋 Prerequisites

- 🐍 Python 3.8+
- 🤖 Telegram bot (create via [@BotFather](https://t.me/botfather))
- 🔑 API keys from RPC providers:
  - [Alchemy](https://www.alchemy.com/) 
  - [Ankr](https://www.ankr.com/)

### ⚡ Local Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your_username/gastracker.git
cd gastracker

# 2️⃣ Create virtual environment  
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the bot
python gas_price_monitor.py
```

## ⚙️ Configuration

Create `.env` file in project root:

```ini
# 🤖 Telegram Configuration
TELEGRAM_BOT_TOKEN="1234567890:ABCDEF1234567890ABCDEF1234567890ABC"
CHAT_ID="@your_channel_name"

# 🌐 RPC Endpoints
RPC_URL_ETH="https://eth-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"
RPC_URL_BLAST="https://rpc.ankr.com/blast/YOUR_ANKR_KEY"
RPC_URL_SCROLL="https://rpc.ankr.com/scroll/YOUR_ANKR_KEY"
RPC_URL_LINEA="https://linea-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"
RPC_URL_BASE="https://base-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"
RPC_URL_STARKNET="https://starknet-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"

# ⚙️ Bot Settings
PHOTO_PATH="static/bot1.jpg"
FOOTER_TEXT="Powered by @devheadb"
SEND_INTERVAL_SECONDS=60
CHECK_INTERVAL_SECONDS=10
GAS_THRESHOLD_OK=15
GAS_THRESHOLD_WARN=25
```

<details>
<summary>📝 Parameter Description</summary>

| Parameter | Description | Example |
|-----------|-------------|---------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token | `1234567890:ABC...` |
| `CHAT_ID` | Channel or chat ID | `@channel_name` or `-100123456789` |
| `SEND_INTERVAL_SECONDS` | Message sending interval (sec) | `60` |
| `CHECK_INTERVAL_SECONDS` | Price checking interval (sec) | `10` |
| `GAS_THRESHOLD_OK` | "Normal" gas threshold (Gwei) | `15` |
| `GAS_THRESHOLD_WARN` | "High" gas threshold (Gwei) | `25` |

</details>

## 🐳 Docker Deployment

<div align="center">

### 🎯 Recommended way for 24/7 operation

</div>

```bash
# 1️⃣ Build image
docker build -t gas-tracker-bot .

# 2️⃣ Run container
docker run -d \
  --name gas-bot \
  --restart unless-stopped \
  --env-file .env \
  gas-tracker-bot
```

### 🛠️ Container Management

```bash
# 📋 View real-time logs
docker logs -f gas-bot

# ⏸️ Stop bot
docker stop gas-bot

# ▶️ Start bot
docker start gas-bot

# 🗑️ Remove container
docker rm gas-bot

# 🔄 Restart with new configuration
docker stop gas-bot && docker rm gas-bot
docker build -t gas-tracker-bot .
docker run -d --name gas-bot --restart unless-stopped --env-file .env gas-tracker-bot
```

## 📱 Message Example

```
⛽ Gas Price Update

🔷 Layer 1 Networks
┌─────────────────────
│ ETH    │ 🟢 12.3 Gwei
│ Blast  │ 🟡 18.7 Gwei
└─────────────────────

🚀 Layer 2 Networks  
┌─────────────────────
│ Scroll │ 🟢 8.1 Gwei
│ Linea  │ 🟢 11.4 Gwei
│ Base   │ 🟢 9.8 Gwei
└─────────────────────

⭐ Other Networks
┌─────────────────────
│ Starknet │ 🟢 6.2 Gwei
└─────────────────────

🕐 Updated: 2024-03-15 14:30:25 UTC
Powered by @devheadb
```

## 🎨 Color Indicators

| Indicator | Meaning | Range |
|-----------|---------|-------|
| 🟢 | Low Gas | < 15 Gwei |
| 🟡 | Medium Gas | 15-25 Gwei |
| 🔴 | High Gas | > 25 Gwei |

## 🔧 Troubleshooting

<details>
<summary>❌ Bot not sending messages</summary>

1. Check `TELEGRAM_BOT_TOKEN` validity
2. Ensure bot is added to channel as administrator
3. Verify `CHAT_ID` correctness

</details>

<details>
<summary>⚠️ RPC connection errors</summary>

1. Verify API key validity
2. Check RPC provider limits  
3. Try alternative RPC endpoints

</details>

<details>
<summary>🐳 Docker issues</summary>

1. Ensure `.env` file is in project root
2. Check Docker daemon is running
3. Rebuild image: `docker build --no-cache -t gas-tracker-bot .`

</details>

## 📈 Monitoring and Logs

```bash
# Check container status
docker ps | grep gas-bot

# View resource usage  
docker stats gas-bot

# Export logs to file
docker logs gas-bot > gas-bot.log 2>&1
```

## 🤝 Contributing

We welcome contributions to the project! 

1. 🍴 Fork the repository
2. 🌿 Create feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit changes (`git commit -m 'Add amazing feature'`)  
4. 📤 Push changes (`git push origin feature/amazing-feature`)
5. 🔄 Create Pull Request

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## 💬 Support

If you have questions or need help:

- 📢 **Telegram Channel**: [Gas Station](https://t.me/gastastion)
- 📧 Email: support@gastrack.com
- 💬 Developer: [@devheadb](https://t.me/devheadb)
- 🐛 Issues: [GitHub Issues](https://github.com/your_username/gastracker/issues)

---

# 🇷🇺 Русская версия

<div align="center">

*Простой и эффективный Python-бот для мониторинга цен на газ в блокчейн-сетях*

**📢 Присоединяйтесь к нашему Telegram каналу: [Gas Station](https://t.me/gastastion)**

[📋 Особенности](#-особенности) • [🚀 Быстрый старт](#-быстрый-старт) • [🐳 Docker](#-развертывание-с-docker) • [⚙️ Настройка](#️-конфигурация)

</div>

---

## 📊 Поддерживаемые сети

<div align="center">

| Сеть | Status | RPC Provider |
|------|--------|--------------|
| 🔷 **Ethereum** | ✅ Active | Alchemy |
| 💥 **Blast** | ✅ Active | Ankr |
| 📜 **Scroll** | ✅ Active | Ankr |  
| 🟢 **Linea** | ✅ Active | Alchemy |
| 🔵 **Base** | ✅ Active | Alchemy |
| ⭐ **Starknet** | ✅ Active | Alchemy |

</div>

## ✨ Особенности

<table>
<tr>
<td>

### 🌐 Мультисетевой мониторинг
Отслеживает цены на газ в 6 основных блокчейн-сетях одновременно

</td>
<td>

### ⚡ Асинхронная архитектура  
Использует `asyncio` для параллельных запросов и высокой производительности

</td>
</tr>
<tr>
<td>

### 💎 Профессиональное оформление
Красиво отформатированные сообщения с эмодзи, разделением по сетям и временными метками

</td>
<td>

### 🛠️ Гибкая настройка
Все параметры легко настраиваются через `.env` файл без изменения кода

</td>
</tr>
<tr>
<td>

### 🐳 Docker Ready
Полностью готов для развертывания в контейнере на любом сервере

</td>
<td>

### 🎯 Умные уведомления
Настраиваемые пороги для предупреждений о высоких ценах на газ

</td>
</tr>
</table>

## 🚀 Быстрый старт

### 📋 Предварительные требования

- 🐍 Python 3.8+
- 🤖 Telegram бот (создать через [@BotFather](https://t.me/botfather))
- 🔑 API ключи от RPC провайдеров:
  - [Alchemy](https://www.alchemy.com/) 
  - [Ankr](https://www.ankr.com/)

### ⚡ Локальная установка

```bash
# 1️⃣ Клонируем репозиторий
git clone https://github.com/your_username/gastracker.git
cd gastracker

# 2️⃣ Создаем виртуальное окружение  
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3️⃣ Устанавливаем зависимости
pip install -r requirements.txt

# 4️⃣ Запускаем бота
python gas_price_monitor.py
```

## ⚙️ Конфигурация

Создайте файл `.env` в корне проекта:

```ini
# 🤖 Telegram Configuration
TELEGRAM_BOT_TOKEN="1234567890:ABCDEF1234567890ABCDEF1234567890ABC"
CHAT_ID="@your_channel_name"

# 🌐 RPC Endpoints
RPC_URL_ETH="https://eth-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"
RPC_URL_BLAST="https://rpc.ankr.com/blast/YOUR_ANKR_KEY"
RPC_URL_SCROLL="https://rpc.ankr.com/scroll/YOUR_ANKR_KEY"
RPC_URL_LINEA="https://linea-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"
RPC_URL_BASE="https://base-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"
RPC_URL_STARKNET="https://starknet-mainnet.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"

# ⚙️ Bot Settings
PHOTO_PATH="static/bot1.jpg"
FOOTER_TEXT="Powered by @devheadb"
SEND_INTERVAL_SECONDS=60
CHECK_INTERVAL_SECONDS=10
GAS_THRESHOLD_OK=15
GAS_THRESHOLD_WARN=25
```

<details>
<summary>📝 Описание параметров</summary>

| Параметр | Описание | Пример |
|----------|----------|--------|
| `TELEGRAM_BOT_TOKEN` | Токен вашего Telegram бота | `1234567890:ABC...` |
| `CHAT_ID` | ID канала или чата | `@channel_name` или `-100123456789` |
| `SEND_INTERVAL_SECONDS` | Интервал отправки сообщений (сек) | `60` |
| `CHECK_INTERVAL_SECONDS` | Интервал проверки цен (сек) | `10` |
| `GAS_THRESHOLD_OK` | Порог "нормального" газа (Gwei) | `15` |
| `GAS_THRESHOLD_WARN` | Порог "высокого" газа (Gwei) | `25` |

</details>

## 🐳 Развертывание с Docker

<div align="center">

### 🎯 Рекомендуемый способ для 24/7 работы

</div>

```bash
# 1️⃣ Собираем образ
docker build -t gas-tracker-bot .

# 2️⃣ Запускаем контейнер
docker run -d \
  --name gas-bot \
  --restart unless-stopped \
  --env-file .env \
  gas-tracker-bot
```

### 🛠️ Управление контейнером

```bash
# 📋 Просмотр логов в реальном времени
docker logs -f gas-bot

# ⏸️ Остановка бота
docker stop gas-bot

# ▶️ Запуск бота
docker start gas-bot

# 🗑️ Удаление контейнера
docker rm gas-bot

# 🔄 Перезапуск с новой конфигурацией
docker stop gas-bot && docker rm gas-bot
docker build -t gas-tracker-bot .
docker run -d --name gas-bot --restart unless-stopped --env-file .env gas-tracker-bot
```

## 📱 Пример сообщения

```
⛽ Gas Price Update

🔷 Layer 1 Networks
┌─────────────────────
│ ETH    │ 🟢 12.3 Gwei
│ Blast  │ 🟡 18.7 Gwei
└─────────────────────

🚀 Layer 2 Networks  
┌─────────────────────
│ Scroll │ 🟢 8.1 Gwei
│ Linea  │ 🟢 11.4 Gwei
│ Base   │ 🟢 9.8 Gwei
└─────────────────────

⭐ Other Networks
┌─────────────────────
│ Starknet │ 🟢 6.2 Gwei
└─────────────────────

🕐 Updated: 2024-03-15 14:30:25 UTC
Powered by @devheadb
```

## 🎨 Цветовые индикаторы

| Индикатор | Значение | Диапазон |
|-----------|----------|----------|
| 🟢 | Низкий газ | < 15 Gwei |
| 🟡 | Средний газ | 15-25 Gwei |
| 🔴 | Высокий газ | > 25 Gwei |

## 🔧 Troubleshooting

<details>
<summary>❌ Бот не отправляет сообщения</summary>

1. Проверьте корректность `TELEGRAM_BOT_TOKEN`
2. Убедитесь, что бот добавлен в канал как администратор
3. Проверьте правильность `CHAT_ID`

</details>

<details>
<summary>⚠️ Ошибки подключения к RPC</summary>

1. Проверьте валидность API ключей
2. Убедитесь в наличии лимитов на RPC провайдере  
3. Попробуйте использовать альтернативные RPC эндпоинты

</details>

<details>
<summary>🐳 Проблемы с Docker</summary>

1. Убедитесь, что `.env` файл находится в корне проекта
2. Проверьте, что Docker daemon запущен
3. Пересоберите образ: `docker build --no-cache -t gas-tracker-bot .`

</details>

## 📈 Мониторинг и логи

```bash
# Просмотр статуса контейнера
docker ps | grep gas-bot

# Просмотр использования ресурсов  
docker stats gas-bot

# Экспорт логов в файл
docker logs gas-bot > gas-bot.log 2>&1
```

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта! 

1. 🍴 Сделайте форк репозитория
2. 🌿 Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`)
3. 💾 Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)  
4. 📤 Отправьте изменения (`git push origin feature/amazing-feature`)
5. 🔄 Создайте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

## 💬 Поддержка

Если у вас есть вопросы или нужна помощь:

- 📢 **Telegram канал**: [Gas Station](https://t.me/gastastion)
- 📧 Email: support@gastrack.com
- 💬 Разработчик: [@devheadb](https://t.me/devheadb)
- 🐛 Issues: [GitHub Issues](https://github.com/your_username/gastracker/issues)

---

<div align="center">

**⭐ Поставьте звезду, если проект был полезен!**

**📢 Следите за обновлениями: [Gas Station](https://t.me/gastastion)**

Made with ❤️ by [@devheadb](https://t.me/devheadb)

</div>

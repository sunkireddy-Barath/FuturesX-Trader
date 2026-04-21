# Binance Futures Testnet Trading Bot

A production-quality CLI-based trading bot for placing MARKET, LIMIT, and STOP-LIMIT orders on Binance Futures Testnet (USDT-M).

## Features

- Place MARKET and LIMIT orders.
- Bonus: Support for STOP-LIMIT orders.
- Supports both BUY and SELL sides.
- Comprehensive CLI input validation.
- Structured logging to both console and `trading_bot.log`.
- Robust error handling for API and network issues.

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py        # Binance client wrapper
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   └── logging_config.py # Logging setup
├── cli.py               # CLI entry point
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd trading_bot
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Credentials**:
   Create a `.env` file in the root directory (where `cli.py` is located) and add your Binance Futures Testnet API keys:
   ```env
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_api_secret
   ```

## Usage

Run the bot using `python cli.py` with the required arguments.

### CLI Arguments

- `--symbol`: Trading symbol (e.g., BTCUSDT)
- `--side`: Side of the trade (`BUY` or `SELL`)
- `--type`: Order type (`MARKET`, `LIMIT`, or `STOP_LIMIT`)
- `--quantity`: Quantity to trade (positive float)
- `--price`: Required for `LIMIT` and `STOP_LIMIT` orders
- `--stop_price`: Required for `STOP_LIMIT` orders

### Example Commands

#### 1. Place a MARKET BUY Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

#### 2. Place a LIMIT SELL Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

#### 3. Place a STOP-LIMIT BUY Order (Bonus)
```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.001 --price 61000 --stop_price 60500
```

## Assumptions

- You have a Binance Futures Testnet account and API keys.
- You are trading USDT-M futures.
- The `python-binance` library handles the underlying REST API calls.
- Environment variables are managed via `python-dotenv`.

## Logging

All requests, responses, and errors are logged to `trading_bot.log`. You can monitor this file in real-time:
```bash
tail -f trading_bot.log
```

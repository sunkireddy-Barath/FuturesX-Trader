# Binance Futures Testnet Trading Bot

A high-quality, production-ready CLI-based trading bot for placing MARKET, LIMIT, and STOP-LIMIT orders on Binance Futures Testnet (USDT-M).

## Key Features

- **Order Types**: Support for MARKET, LIMIT, and STOP-LIMIT orders.
- **Interactive Mode**: Guided menu-driven order placement (`--interactive`).
- **Advanced Controls**: Set Leverage (1-125x) and Margin Type (ISOLATED/CROSS).
- **Validation**: Robust CLI input validation and real-time feedback.
- **Logging**: Detailed structured logging to both console and `trading_bot.log`.
- **Testing**: Built-in unit tests for core validation logic.

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py        # Binance API wrapper with leverage/margin support
│   ├── config.py        # Centralized configuration management
│   ├── orders.py        # Order execution and display logic
│   ├── validators.py    # CLI and business logic validation
│   └── logging_config.py # Structured logging setup
├── tests/
│   ├── __init__.py
│   └── test_validators.py # Unit tests for validation logic
├── cli.py               # Main CLI entry point (supports args & interactive)
├── simulation.py        # Mock simulation for log generation
├── trading_bot.log      # Sample log file (Market & Limit orders)
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd trading_bot
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Credentials**:
   Copy `.env.example` to `.env` and add your Binance Futures Testnet API keys:
   ```bash
   cp .env.example .env
   # Edit .env with your keys
   ```

## Usage

### 1. Interactive Mode (Recommended)
Guided mode that prompts you for all necessary information:
```bash
python cli.py --interactive
```

### 2. Command Line Arguments
Place orders directly via CLI flags:

- **MARKET Order**:
  ```bash
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
  ```

- **LIMIT Order**:
  ```bash
  python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
  ```

- **Advanced Options** (Leverage & Margin):
  ```bash
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001 --leverage 10 --margin_type ISOLATED
  ```

## Running Tests

Verify the validation logic using the built-in tests:
```bash
PYTHONPATH=. python3 tests/test_validators.py
```

## Verification and Logs

- **`simulation.py`**: Use this to generate sample logs without real API keys.
- **`trading_bot.log`**: Sample logs included for MARKET and LIMIT orders as per assignment deliverables.

## Assumptions

- Trading strictly on **USDT-M Futures Testnet**.
- Environment variables are managed via `python-dotenv`.
- The bot handles `BinanceAPIException` for common issues like insufficient margin or invalid symbols.

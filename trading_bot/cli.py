import os
import argparse
import sys
from dotenv import load_dotenv
from bot.logging_config import setup_logging
from bot.validators import validate_order_input, validate_positive_float
from bot.client import BinanceFuturesClient
from bot.orders import execute_order

# Load environment variables from .env file
load_dotenv()

def main():
    # Setup logging
    logger = setup_logging()
    logger.info("Starting Trading Bot CLI...")

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    # Required arguments
    parser.add_argument("--symbol", type=str, required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=['BUY', 'SELL'], help="Order side (BUY or SELL)")
    parser.add_argument("--type", type=str, required=True, choices=['MARKET', 'LIMIT', 'STOP_LIMIT'], help="Order type (MARKET, LIMIT, or STOP_LIMIT)")
    parser.add_argument("--quantity", type=validate_positive_float, required=True, help="Order quantity")
    
    # Optional arguments
    parser.add_argument("--price", type=validate_positive_float, help="Order price (required for LIMIT/STOP_LIMIT)")
    parser.add_argument("--stop_price", type=validate_positive_float, help="Stop price (required for STOP_LIMIT)")

    args = parser.parse_args()

    # 1. Custom validation
    if not validate_order_input(args):
        sys.exit(1)

    # 2. Get API credentials
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        logger.error("API credentials missing. Please set BINANCE_API_KEY and BINANCE_API_SECRET in your .env file or environment.")
        print("Error: API credentials missing. Check logs or .env file.")
        sys.exit(1)

    # 3. Initialize Client
    bot_client = BinanceFuturesClient(api_key, api_secret)
    if not bot_client.connect():
        sys.exit(1)

    # 4. Execute Order
    success = execute_order(
        client=bot_client,
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price,
        stop_price=args.stop_price
    )

    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()

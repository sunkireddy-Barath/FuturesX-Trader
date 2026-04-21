import os
import argparse
import sys
from bot.config import Config
from bot.logging_config import setup_logging
from bot.validators import validate_order_input, validate_positive_float
from bot.client import BinanceFuturesClient
from bot.orders import execute_order

def run_interactive_mode(bot_client):
    """
    Runs a menu-driven interactive mode for order placement.
    """
    print("\n=== Interactive Trading Mode ===")
    try:
        symbol = input(f"Enter symbol (default {Config.DEFAULT_SYMBOL}): ").upper() or Config.DEFAULT_SYMBOL
        side = input("Enter side (BUY/SELL): ").upper()
        while side not in ['BUY', 'SELL']:
            side = input("Invalid side. Enter BUY or SELL: ").upper()
            
        order_type = input("Enter type (MARKET/LIMIT/STOP_LIMIT): ").upper()
        while order_type not in ['MARKET', 'LIMIT', 'STOP_LIMIT']:
            order_type = input("Invalid type. Enter MARKET, LIMIT, or STOP_LIMIT: ").upper()
            
        quantity = float(input("Enter quantity: "))
        
        price = None
        if order_type in ['LIMIT', 'STOP_LIMIT']:
            price = float(input("Enter price: "))
            
        stop_price = None
        if order_type == 'STOP_LIMIT':
            stop_price = float(input("Enter stop price: "))
            
        leverage = input(f"Enter leverage (default {Config.DEFAULT_LEVERAGE}): ")
        leverage = int(leverage) if leverage else Config.DEFAULT_LEVERAGE
        
        margin_type = input(f"Enter margin type (ISOLATED/CROSS, default {Config.DEFAULT_MARGIN_TYPE}): ").upper()
        margin_type = margin_type if margin_type else Config.DEFAULT_MARGIN_TYPE

        # Confirm and Execute
        print(f"\nOrder Summary: {side} {quantity} {symbol} at {order_type} (Lev: {leverage}x, Margin: {margin_type})")
        confirm = input("Confirm order? (y/n): ").lower()
        
        if confirm == 'y':
            execute_order(
                client=bot_client,
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price,
                stop_price=stop_price,
                leverage=leverage,
                margin_type=margin_type
            )
        else:
            print("Order cancelled.")

    except ValueError as e:
        print(f"Error: Invalid input. {str(e)}")
    except KeyboardInterrupt:
        print("\nInteractive mode exited.")

def main():
    # Setup logging
    logger = setup_logging()
    logger.info("Starting Trading Bot CLI...")

    # Load and validate config
    is_valid, error_msg = Config.validate()
    if not is_valid:
        logger.error(error_msg)
        print(f"Error: {error_msg}")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    # Optional Interactive Mode
    parser.add_argument("--interactive", action="store_true", help="Run in interactive menu mode")
    
    # Standard arguments
    parser.add_argument("--symbol", type=str, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, choices=['BUY', 'SELL'], help="Order side (BUY or SELL)")
    parser.add_argument("--type", type=str, choices=['MARKET', 'LIMIT', 'STOP_LIMIT'], help="Order type")
    parser.add_argument("--quantity", type=validate_positive_float, help="Order quantity")
    parser.add_argument("--price", type=validate_positive_float, help="Order price")
    parser.add_argument("--stop_price", type=validate_positive_float, help="Stop price")
    parser.add_argument("--leverage", type=int, default=Config.DEFAULT_LEVERAGE, help="Leverage (1-125)")
    parser.add_argument("--margin_type", type=str, choices=['ISOLATED', 'CROSS'], default=Config.DEFAULT_MARGIN_TYPE, help="Margin type")

    args = parser.parse_args()

    # Initialize Client
    bot_client = BinanceFuturesClient(Config.API_KEY, Config.API_SECRET)
    if not bot_client.connect():
        sys.exit(1)

    if args.interactive:
        run_interactive_mode(bot_client)
    else:
        # Check for required arguments in non-interactive mode
        required = ['symbol', 'side', 'type', 'quantity']
        missing = [arg for arg in required if getattr(args, arg) is None]
        if missing:
            parser.error(f"The following arguments are required: {', '.join(['--'+m for m in missing])}")

        if not validate_order_input(args):
            sys.exit(1)

        execute_order(
            client=bot_client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stop_price,
            leverage=args.leverage,
            margin_type=args.margin_type
        )

if __name__ == "__main__":
    main()

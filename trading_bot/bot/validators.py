import argparse
import sys

def validate_positive_float(value):
    """
    Validates that a value is a positive float.
    """
    try:
        fvalue = float(value)
        if fvalue <= 0:
            raise argparse.ArgumentTypeError(f"{value} is an invalid positive float value")
        return fvalue
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid float")

def validate_order_input(args):
    """
    Performs custom validation for the order arguments.
    """
    # 1. Check side
    if args.side.upper() not in ['BUY', 'SELL']:
        print(f"Error: Invalid side '{args.side}'. Must be BUY or SELL.")
        return False

    # 2. Check type
    if args.type.upper() not in ['MARKET', 'LIMIT', 'STOP_LIMIT']:
        print(f"Error: Invalid type '{args.type}'. Must be MARKET, LIMIT, or STOP_LIMIT.")
        return False

    # 3. Check quantity
    if args.quantity <= 0:
        print(f"Error: Quantity must be greater than 0.")
        return False

    # 4. Check price for LIMIT and STOP_LIMIT orders
    if args.type.upper() in ['LIMIT', 'STOP_LIMIT']:
        if args.price is None:
            print(f"Error: Price is required for {args.type} orders.")
            return False
        if args.price <= 0:
            print(f"Error: Price must be greater than 0.")
            return False

    # 5. Check stop price for STOP_LIMIT orders (Bonus requirement)
    if args.type.upper() == 'STOP_LIMIT':
        if getattr(args, 'stop_price', None) is None:
            print(f"Error: Stop price is required for STOP_LIMIT orders.")
            return False
    
    return True

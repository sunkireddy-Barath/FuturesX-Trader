import logging
import sys

logger = logging.getLogger(__name__)

def execute_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    """
    Coordinates the order placement and prints the required output.
    """
    print("\n--- Order Summary ---")
    print(f"Symbol:   {symbol}")
    print(f"Side:     {side.upper()}")
    print(f"Type:     {order_type.upper()}")
    print(f"Quantity: {quantity}")
    if price:
        print(f"Price:    {price}")
    if stop_price:
        print(f"Stop:     {stop_price}")
    print("---------------------\n")

    try:
        response = client.create_futures_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        print("SUCCESS: Order placed successfully.")
        print("\n--- Response Details ---")
        print(f"OrderID:      {response.get('orderId')}")
        print(f"Status:       {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price:    {response.get('avgPrice', 'N/A')}")
        print("------------------------\n")
        
        return True

    except Exception as e:
        print(f"FAILURE: Could not place order. Error: {str(e)}")
        # The error is already logged in client.py
        return False

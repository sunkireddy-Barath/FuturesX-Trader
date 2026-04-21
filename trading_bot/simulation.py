import os
import sys
import logging
from unittest.mock import MagicMock
import bot.client
import bot.orders
from bot.logging_config import setup_logging

# Setup logging
setup_logging('trading_bot.log')
logger = logging.getLogger('simulation')

def run_simulation():
    print("Starting simulation to generate sample logs...")
    
    # Mock the Binance Client
    mock_client_instance = MagicMock()
    
    # MARKET order success response
    market_response = {
        'orderId': 12345678,
        'status': 'FILLED',
        'executedQty': '0.10000000',
        'avgPrice': '65000.50',
        'symbol': 'BTCUSDT',
        'side': 'BUY',
        'type': 'MARKET'
    }
    
    # LIMIT order success response
    limit_response = {
        'orderId': 87654321,
        'status': 'NEW',
        'executedQty': '0.00000000',
        'avgPrice': '0.00',
        'symbol': 'BTCUSDT',
        'side': 'SELL',
        'type': 'LIMIT'
    }

    # Create the wrapper client with the mock
    bot_client = bot.client.BinanceFuturesClient("mock_key", "mock_secret")
    bot_client.client = mock_client_instance
    
    # 1. Simulate MARKET BUY Order with Leverage
    print("\n--- Simulating MARKET BUY Order with Leverage ---")
    mock_client_instance.futures_create_order.return_value = market_response
    
    bot.orders.execute_order(
        bot_client, "BTCUSDT", "BUY", "MARKET", 0.1, leverage=10, margin_type="ISOLATED"
    )

    # 2. Simulate LIMIT SELL Order
    print("\n--- Simulating LIMIT SELL Order ---")
    mock_client_instance.futures_create_order.return_value = limit_response
    
    bot.orders.execute_order(
        bot_client, "BTCUSDT", "SELL", "LIMIT", 0.05, price=60000
    )

    print("\nSimulation complete. 'trading_bot.log' has been updated.")

if __name__ == "__main__":
    # Add project root to path so we can import bot
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    run_simulation()

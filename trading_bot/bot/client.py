import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    """
    A wrapper class for the Binance Futures Testnet client.
    """
    def __init__(self, api_key, api_secret):
        """
        Initializes the Binance client with testnet=True.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = None

    def connect(self):
        """
        Connects to the Binance Futures Testnet.
        """
        try:
            # For Testnet, we set testnet=True
            self.client = Client(self.api_key, self.api_secret, testnet=True)
            logger.info("Successfully connected to Binance Futures Testnet API.")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Binance API: {str(e)}")
            return False

    def set_margin_type(self, symbol, margin_type):
        """
        Sets the margin type for the symbol (ISOLATED or CROSSED).
        """
        try:
            response = self.client.futures_change_margin_type(symbol=symbol, marginType=margin_type.upper())
            logger.info(f"Margin type set to {margin_type} for {symbol}: {response}")
            return response
        except BinanceAPIException as e:
            if "No need to change margin type" in e.message:
                logger.info(f"Margin type is already {margin_type} for {symbol}.")
                return None
            logger.error(f"Failed to set margin type: {e.message}")
            raise

    def set_leverage(self, symbol, leverage):
        """
        Sets the leverage for the symbol.
        """
        try:
            response = self.client.futures_change_leverage(symbol=symbol, leverage=leverage)
            logger.info(f"Leverage set to {leverage} for {symbol}: {response}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Failed to set leverage: {e.message}")
            raise

    def create_futures_order(self, symbol, side, type, quantity, price=None, stop_price=None, leverage=None, margin_type=None):
        """
        Places a futures order on USDT-M testnet.
        """
        try:
            # Optionally set leverage and margin type if provided
            if margin_type:
                self.set_margin_type(symbol, margin_type)
            if leverage:
                self.set_leverage(symbol, leverage)

            params = {
                'symbol': symbol,
                'side': side.upper(),
                'type': type.upper(),
                'quantity': quantity
            }

            if type.upper() == 'LIMIT':
                params['price'] = str(price)
                params['timeInForce'] = 'GTC'  # Good Till Cancelled
            elif type.upper() == 'STOP_LIMIT':
                params['price'] = str(price)
                params['stopPrice'] = str(stop_price)
                params['timeInForce'] = 'GTC'

            logger.info(f"Sending order request: {params}")
            
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order response received: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Exception: {e.status_code} - {e.message}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Binance Request Exception: {e.message}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")
            raise

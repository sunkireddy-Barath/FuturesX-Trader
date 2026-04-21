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

    def create_futures_order(self, symbol, side, type, quantity, price=None, stop_price=None):
        """
        Places a futures order on USDT-M testnet.
        """
        try:
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

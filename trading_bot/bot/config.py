import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """
    Centralized configuration for the trading bot.
    """
    API_KEY = os.getenv("BINANCE_API_KEY")
    API_SECRET = os.getenv("BINANCE_API_SECRET")
    
    # Defaults
    DEFAULT_SYMBOL = "BTCUSDT"
    DEFAULT_LEVERAGE = 1
    DEFAULT_MARGIN_TYPE = "ISOLATED"  # ISOLATED or CROSS
    
    @classmethod
    def validate(cls):
        """
        Validates that required configuration is present.
        """
        if not cls.API_KEY or not cls.API_SECRET:
            return False, "API credentials missing. Please set BINANCE_API_KEY and BINANCE_API_SECRET."
        return True, ""

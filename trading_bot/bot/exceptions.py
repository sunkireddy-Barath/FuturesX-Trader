class TradingBotError(Exception):
    """Base class for exceptions in this module."""
    pass

class ValidationError(TradingBotError):
    """Exception raised for errors in the input validation."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ClientConnectionError(TradingBotError):
    """Exception raised when the Binance API connection fails."""
    pass

class OrderExecutionError(TradingBotError):
    """Exception raised when an order fails to execute."""
    pass

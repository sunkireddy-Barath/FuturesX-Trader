import unittest
import argparse
from bot.validators import validate_positive_float, validate_order_input

class TestValidators(unittest.TestCase):
    def test_validate_positive_float_success(self):
        self.assertEqual(validate_positive_float("10.5"), 10.5)
        self.assertEqual(validate_positive_float(5), 5.0)

    def test_validate_positive_float_failure(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            validate_positive_float("-1")
        with self.assertRaises(argparse.ArgumentTypeError):
            validate_positive_float("abc")

    def test_validate_order_input_market_success(self):
        args = argparse.Namespace(
            side="BUY",
            type="MARKET",
            quantity=1.0,
            symbol="BTCUSDT",
            price=None
        )
        self.assertTrue(validate_order_input(args))

    def test_validate_order_input_limit_failure_no_price(self):
        args = argparse.Namespace(
            side="BUY",
            type="LIMIT",
            quantity=1.0,
            symbol="BTCUSDT",
            price=None
        )
        # validate_order_input returns False on failure
        self.assertFalse(validate_order_input(args))

    def test_validate_order_input_invalid_side(self):
        args = argparse.Namespace(
            side="HOLD",
            type="MARKET",
            quantity=1.0,
            symbol="BTCUSDT",
            price=None
        )
        self.assertFalse(validate_order_input(args))

if __name__ == "__main__":
    unittest.main()

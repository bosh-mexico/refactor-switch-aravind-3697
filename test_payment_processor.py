import unittest
from payment_processor import PaymentMode, checkout

class TestPaymentProcessor(unittest.TestCase):

    def test_paypal(self):
        checkout(PaymentMode.PAYPAL, 100)

    def test_googlepay(self):
        checkout(PaymentMode.GOOGLEPAY, 200)

    def test_creditcard(self):
        checkout(PaymentMode.CREDITCARD, 300)

    def test_invalid_mode(self):
        checkout(PaymentMode.UNKNOWN, 400)

    def test_invalid_amount(self):
        checkout(PaymentMode.PAYPAL, -10)

if __name__ == "__main__":
    unittest.main()

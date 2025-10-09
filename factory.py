from paypal import PayPalProcessor
from googlepay import GooglePayProcessor
from creditcard import CreditCardProcessor

class PaymentFactory:
    @staticmethod
    def get_processor(payment_type: str):
        processors = {
            "paypal": PayPalProcessor(),
            "googlepay": GooglePayProcessor(),
            "creditcard": CreditCardProcessor(),
        }
        return processors.get(payment_type.lower(), None)

from base import PaymentProcessor

class PayPalProcessor(PaymentProcessor):

    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")
        print("   -> Placeholder: Connect to PayPal API.")

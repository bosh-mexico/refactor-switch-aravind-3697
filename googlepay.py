from base import PaymentProcessor

class GooglePayProcessor(PaymentProcessor):

    def process_payment(self, amount: float):
        print(f"Processing Google Pay payment of ${amount:.2f}")
        print("   -> Placeholder: Connect to Google Pay API.")

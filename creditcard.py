from base import PaymentProcessor

class CreditCardProcessor(PaymentProcessor):
  
    def process_payment(self, amount: float):
        print(f"Processing Credit Card payment of ${amount:.2f}")
        print("   -> Placeholder: Connect to Credit Card Gateway.")

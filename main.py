from payment_processor.factory import PaymentFactory

def checkout(payment_type: str, amount: float):
    if amount <= 0:
        print("❌ Invalid payment amount.")
        return

    processor = PaymentFactory.get_processor(payment_type)
    if processor:
        processor.process_payment(amount)
    else:
        print(f"❌ Unsupported payment mode: '{payment_type}'")


if __name__ == "__main__":
    checkout("paypal", 150.00)
    checkout("googlepay", 200.00)
    checkout("creditcard", 300.00)
    checkout("applepay", 400.00)  # unsupported example

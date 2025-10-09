from factory import PaymentFactory

def checkout(payment_type: str, amount: float):
    if amount <= 0:
        print("Invalid payment amount.")
        return

    processor = PaymentFactory.get_processor(payment_type)
    if processor:
        processor.process_payment(amount)
    else:
        print(f"Unsupported payment mode: '{payment_type}'")

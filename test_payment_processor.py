from payment_processor.factory import PaymentFactory

def test_payment_modes():
    for mode in ["paypal", "googlepay", "creditcard", "applepay"]:
        print(f"\nTesting mode: {mode}")
        processor = PaymentFactory.get_processor(mode)
        if processor:
            processor.process_payment(100)
        else:
            print("❌ No processor available")

if __name__ == "__main__":
    test_payment_modes()

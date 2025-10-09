from payment_processor import checkout

def run_tests():
    print("\n--- Running Payment Processor Tests ---")
    test_cases = [
        ("paypal", 100.00),
        ("googlepay", 200.00),
        ("creditcard", 300.00),
        ("applepay", 400.00),   # Unsupported
        ("paypal", -50.00),     # Invalid amount
    ]

    for mode, amount in test_cases:
        print(f"\n[Test] Mode: {mode}, Amount: {amount}")
        checkout(mode, amount)


if __name__ == "__main__":
    run_tests()

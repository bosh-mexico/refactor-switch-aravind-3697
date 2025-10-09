from payment_processor import checkout

if __name__ == "__main__":
    print("\n--- Payment Checkout Simulation ---\n")
    checkout("paypal", 150.00)
    checkout("googlepay", 200.00)
    checkout("creditcard", 300.00)
    checkout("applepay", 400.00)  # Unsupported mode

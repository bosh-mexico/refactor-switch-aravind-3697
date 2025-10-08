from enum import Enum

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99


def checkout(mode: PaymentMode, amount: float):
    # Validate amount
    if amount <= 0:
        print("❌ Error: Invalid payment amount. Please enter a positive value.")
        return

    # Process based on mode
    match mode:
        case PaymentMode.PAYPAL:
            print(f"Processing PayPal payment of ${amount:.2f}")
            print("   -> Connecting to PayPal API... (placeholder logic)")

        case PaymentMode.GOOGLEPAY:
            print(f"Processing Google Pay payment of ${amount:.2f}")
            print("   -> Connecting to Google Pay API... (placeholder logic)")

        case PaymentMode.CREDITCARD:
            print(f"Processing Credit Card payment of ${amount:.2f}")
            print("   -> Connecting to Credit Card gateway... (placeholder logic)")

        case _:
            print("Error: Unsupported or invalid payment mode selected!")

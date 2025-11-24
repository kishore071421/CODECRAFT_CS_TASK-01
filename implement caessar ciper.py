def caesar_shift(char, shift):
    """Shift a single character (helper function)."""
    if not char.isalpha():
        return char

    shift %= 26  # Normalize shift

    base = 65 if char.isupper() else 97
    return chr((ord(char) - base + shift) % 26 + base)


def encrypt(text, shift):
    """Encrypt text using Caesar Cipher."""
    return "".join(caesar_shift(c, shift) for c in text)


def decrypt(text, shift):
    """Decrypt text using Caesar Cipher."""
    return encrypt(text, -shift)


def get_int(prompt):
    """Safely get an integer input from user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def print_menu():
    """Display the program menu."""
    print("\n=== Caesar Cipher Tool ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice in {"1", "2"}:
            message = input("Enter your message: ")
            shift = get_int("Enter shift value: ")

            if choice == "1":
                print("Encrypted Message:", encrypt(message, shift))
            else:
                print("Decrypted Message:", decrypt(message, shift))

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()

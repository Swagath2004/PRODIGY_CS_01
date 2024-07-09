def encrypt(shift, text):
    result = ""
    for letter in text:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def decrypt(shift, text):
    result = ""
    for letter in text:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice in ['E', 'D']:
            text = input("Enter the text: ")
            shift = get_valid_int("Enter the shift value: ")
            if choice == 'E':
                result = encrypt(shift, text)
                print("Encrypted text:", result)
            else:
                result = decrypt(shift, text)
                print("Decrypted text:", result)
        else:
            print("Invalid choice. Please choose 'E' for encrypt or 'D' for decrypt.")

        cont = input("Do you want to continue? (Y/N): ").upper()
        if cont != 'Y':
            print("Thank you for using the Caesar Cipher Program! Goodbye!")
            break

if __name__ == "__main__":
    main()

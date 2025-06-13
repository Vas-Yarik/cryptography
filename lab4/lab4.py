from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os


def encrypt_file(input_file, output_file, key):
    if len(key) != 8:
        print("Error: key must be exactly 8 characters!")
        return

    iv = os.urandom(8)
    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)

    with open(input_file, 'rb') as f:
        plaintext = f.read()

    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)

    print(f"File encrypted: {output_file}")


def decrypt_file(input_file, output_file, key):
    if len(key) != 8:
        print("Error: key must be exactly 8 characters!")
        return

    with open(input_file, 'rb') as f:
        data = f.read()

    iv = data[:8]
    ciphertext = data[8:]

    cipher = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv)

    try:
        plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)

        with open(output_file, 'wb') as f:
            f.write(plaintext)

        print(f"File decrypted: {output_file}")
    except ValueError:
        print("Error: invalid key or corrupted file!")


def main():
    while True:
        print("\nMenu: ")
        print("1. Encrypt file")
        print("2. Decrypt file")
        print("3. Exit")
        choice = input("\nChoose an action: ").strip()

        if choice == "1":
            input_file = input("Input file: ")
            output_file = input("Output file: ")
            key = input("Key (exactly 8 characters): ")
            encrypt_file(input_file, output_file, key)

        elif choice == "2":
            input_file = input("Input file: ")
            output_file = input("Output file: ")
            key = input("Key (exactly 8 characters): ")
            decrypt_file(input_file, output_file, key)

        elif choice == "3":
            print("Exiting the program")
            break

        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

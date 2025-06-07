import os


def create_text_file(file_path):
    print("\nEnter text to save to the file (press Enter twice to finish):")
    text = []
    while True:
        line = input()
        if line == "":
            break
        text.append(line)

    full_text = '\n'.join(text)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"\nText saved to file: {file_path} ({len(full_text)} characters)")


def generate_key(file_path, size):
    key = os.urandom(size)
    with open(file_path, 'wb') as f:
        f.write(key)
    print(f"Key generated: {file_path} ({size} bytes)")


def vernam_cipher(input_file, key_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    with open(key_file, 'rb') as f:
        key = f.read()

    if len(data) > len(key):
        raise ValueError("Error: key must be at least as long as the data!")

    result = bytes([a ^ b for a, b in zip(data, key)])

    with open(output_file, 'wb') as f:
        f.write(result)
    print(f"Result saved to {output_file}")


class SimpleRC4:
    def __init__(self, key):
        self.S = list(range(256))
        j = 0

        for i in range(256):
            j = (j + self.S[i] + key[i % len(key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
        self.i = self.j = 0

    def encrypt(self, data):
        result = []
        for byte in data:
            self.i = (self.i + 1) % 256
            self.j = (self.j + self.S[self.i]) % 256
            self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
            k = self.S[(self.S[self.i] + self.S[self.j]) % 256]
            result.append(byte ^ k)
        return bytes(result)

def main_menu():
    print("\nMenu: ")
    print("1. Create text file")
    print("2. Generate key")
    print("3. Vernam cipher")
    print("4. RC4 encryption")
    print("0. Exit")


def main():
    while True:
        main_menu()
        choice = input("\nChoose an action: ").strip()

        if choice == "1":
            file_path = input("Enter the filename to save: ")
            create_text_file(file_path)

        elif choice == "2":
            file_path = input("Filename for the key: ")
            size = int(input("Key size (bytes): "))
            generate_key(file_path, size)

        elif choice == "3":
            input_file = input("File with data: ")
            key_file = input("File with key: ")
            output_file = input("Output file: ")
            try:
                vernam_cipher(input_file, key_file, output_file)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            input_file = input("File with data: ")
            key = input("Key (string): ").encode('utf-8')
            output_file = input("Output file: ")

            with open(input_file, 'rb') as f:
                data = f.read()

            cipher = SimpleRC4(key)
            result = cipher.encrypt(data)

            with open(output_file, 'wb') as f:
                f.write(result)
            print(f"Result saved to {output_file}")

        elif choice == "0":
            print("Exiting the program")
            break

        else:
            print("Invalid choice!")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

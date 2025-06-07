import math
import os
import random
from collections import Counter


def calculate_frequencies(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    total_chars = len(data)
    frequencies = Counter(data)
    return {char: count / total_chars for char, count in frequencies.items()}


def calculate_entropy(frequencies):
    entropy = 0.0
    for freq in frequencies.values():
        if freq > 0:
            entropy -= freq * math.log2(freq)
    return entropy


def generate_file(file_path, file_type, size=1024, char=None):
    if file_type == 1:
        if not char:
            char = input("Enter a character to repeat: ")[0]
        data = char.encode() * size
    elif file_type == 2:
        data = ''.join(random.choice('01') for _ in range(size)).encode()
    elif file_type == 3:
        data = bytes([random.randint(32, 126) for _ in range(size)])
    elif file_type == 4:
        text = " ".join(["hello"] * (size // 6))
        data = text.encode()[:size]
    elif file_type == 5:
        text = " ".join(["hello"] * (size // 7))  # Translated "привет" to "hello"
        data = text.encode()[:size]

    with open(file_path, 'wb') as file:
        file.write(data)
    print(f"File {file_path} successfully created ({size} bytes)")


def main_menu():
    print("\nMenu: ")
    print("1. Analyze existing file")
    print("2. Generate test file")
    print("0. Exit")


def file_analysis_menu():
    file_path = input("Enter the path to the file: ")

    if not os.path.exists(file_path):
        print("Error: file does not exist")
        return

    try:
        frequencies = calculate_frequencies(file_path)
        entropy = calculate_entropy(frequencies)

        print("\nAnalysis results:")
        print(f"File size: {os.path.getsize(file_path)} bytes")
        print(f"Unique characters: {len(frequencies)}")
        print(f"Entropy: {entropy:.4f} bits/character")

    except Exception as e:
        print(f"Error analyzing the file: {e}")


def generate_file_menu():
    print("1. File from repeating character")
    print("2. Random '0's and '1's")
    print("3. Random printable ASCII characters")
    print("4. Text in English")
    print("5. Text in Russian")

    choice = input("\nChoose file type (1-5): ")
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice")
        return

    file_path = input("Enter the filename to save: ")
    size = input("Enter the file size in bytes (default 1024): ")
    try:
        size = int(size) if size else 1024
    except ValueError:
        print("Invalid size, using 1024 bytes")
        size = 1024

    generate_file(file_path, int(choice), size)


def main():
    while True:
        main_menu()
        choice = input("\nChoose an action: ")

        if choice == '1':
            file_analysis_menu()
        elif choice == '2':
            generate_file_menu()
        elif choice == '0':
            print("Exiting the program")
            break
        else:
            print("Invalid choice, please try again")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
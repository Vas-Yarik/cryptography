import nltk
nltk.download('words')

def caesar_encrypt(text: str, key: int) -> str:
    encrypted = []
    for char in text:
        if char.isalpha():
            shifted = (ord(char.lower()) - ord('a') + key) % 26
            encrypted.append(chr(shifted + ord('a')))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def caesar_decrypt(text: str, key: int) -> str:
    return caesar_encrypt(text, -key)

def find_key(plaintext: str, ciphertext: str) -> int:
    if len(plaintext) == 0 or len(ciphertext) == 0:
        return 0
    p_char = plaintext[0].lower()
    c_char = ciphertext[0].lower()
    if not p_char.isalpha() or not c_char.isalpha():
        return 0
    return (ord(c_char) - ord(p_char)) % 26

def brute_force_caesar(ciphertext: str):
    for key in range(26):
        decrypted = caesar_decrypt(ciphertext, key)
        print(f"Key {key}: {decrypted}")

def auto_decrypt(ciphertext: str) -> int:
    word_set = set(nltk.corpus.words.words())
    best_key = 0
    max_matches = 0
    for key in range(26):
        decrypted = caesar_decrypt(ciphertext, key)
        decrypted_words = decrypted.split()
        matches = sum(word.lower() in word_set for word in decrypted_words)
        if matches > max_matches:
            max_matches = matches
            best_key = key
    return best_key

def main():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Unknown text attack")
    print("4. Full search")
    print("5. Auto decrypt")
    print("0. Exit")
    choice = input("\nEnter: : ").strip()

    if choice == "1":
        text = input("Text: ")
        key = int(input("Key (0-25): "))
        print(f"Result: {caesar_encrypt(text, key)}")

    elif choice == "2":
        text = input("Text: ")
        key = int(input("Key (0-25): "))
        print(f"Result: {caesar_decrypt(text, key)}")

    elif choice == "3":
        plaintext = input("Source text: ")
        ciphertext = input("Encrypt text: ")
        key = find_key(plaintext, ciphertext)
        print(f"Key is: {key}")

    elif choice == "4":
        ciphertext = input("Encrypt text: ")
        brute_force_caesar(ciphertext)

    elif choice == "5":
        ciphertext = input("Encrypt text: ")
        key = auto_decrypt(ciphertext)
        decrypted = caesar_decrypt(ciphertext, key)
        print(f"Key is: {key}")
        print(f"Decrypt text: {decrypted}")

    else:
        print("Error")

if __name__ == "__main__":
    main()
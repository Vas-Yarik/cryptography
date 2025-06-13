import hashlib
import itertools
import string

def sha256_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

def partial_preimage(target_prefix, max_length=5):
    characters = string.ascii_letters + string.digits
    for length in range(1, max_length + 1):
        for candidate in itertools.product(characters, repeat=length):
            candidate_string = ''.join(candidate)
            if sha256_hash(candidate_string).startswith(target_prefix):
                return candidate_string
    return None

def main():
    target_prefix = input("Enter the target prefix to search for (e.g., 'abc'): ")
    max_length = int(input("Enter the maximum length of the string to search for: "))
    
    result = partial_preimage(target_prefix, max_length)
    
    if result:
        print(f"Found corresponding value: {result} -> SHA-256: {sha256_hash(result)}")
    else:
        print("Could not find a corresponding value.")

if __name__ == "__main__":
    main()

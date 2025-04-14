from vigenere import encrypt_vigenere, decrypt_vigenere

def main():
    plaintext = "HELLO, WORLD!"
    key = "KEY"

    encrypted = encrypt_vigenere(plaintext, key)
    decrypted = decrypt_vigenere(encrypted, key)

    print("🔐 Vigenere Cipher")
    print(f"Plaintext : {plaintext}")
    print(f"Key       : {key}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")

if __name__ == "__main__":
    main()

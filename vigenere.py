def repeat_key(key, length):
    return (key * (length // len(key) + 1))[:length]

def encrypt_vigenere(plaintext, key):
    key = repeat_key(key.upper(), len(plaintext))
    ciphertext = ""
    for p, k in zip(plaintext.upper(), key):
        if p.isalpha():
            c = chr(((ord(p) - ord('A') + ord(k) - ord('A')) % 26) + ord('A'))
            ciphertext += c
        else:
            ciphertext += p
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    key = repeat_key(key.upper(), len(ciphertext))
    plaintext = ""
    for c, k in zip(ciphertext.upper(), key):
        if c.isalpha():
            p = chr(((ord(c) - ord(k) + 26) % 26) + ord('A'))
            plaintext += p
        else:
            plaintext += c
    return plaintext

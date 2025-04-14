import unittest
from vigenere import encrypt_vigenere, decrypt_vigenere

class TestVigenereCipher(unittest.TestCase):

    # --- Проверка encrypt по известным данным ---
    def test_encrypt_known_1(self):
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    def test_encrypt_known_2(self):
        self.assertEqual(encrypt_vigenere("HELLO", "KEY"), "RIJVS")

    def test_encrypt_case_insensitivity(self):
        self.assertEqual(encrypt_vigenere("hello", "key"), "RIJVS")

    # --- Проверка decrypt по известным данным ---
    def test_decrypt_known_1(self):
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_decrypt_known_2(self):
        self.assertEqual(decrypt_vigenere("RIJVS", "KEY"), "HELLO")

    def test_decrypt_case_insensitivity(self):
        self.assertEqual(decrypt_vigenere("rijvs", "key"), "HELLO")

    # --- Согласованное шифрование-дешифрование ---
    def test_encrypt_decrypt_simple(self):
        text = "HELLO, WORLD!"
        key = "KEY"
        encrypted = encrypt_vigenere(text, key)
        decrypted = decrypt_vigenere(encrypted, key)
        self.assertEqual(decrypted, text.upper())

    def test_encrypt_decrypt_with_numbers_symbols(self):
        text = "ENCRYPT 123!@#"
        key = "SECRET"
        encrypted = encrypt_vigenere(text, key)
        decrypted = decrypt_vigenere(encrypted, key)
        self.assertEqual(decrypted, text.upper())

    def test_encrypt_decrypt_empty_string(self):
        self.assertEqual(encrypt_vigenere("", "KEY"), "")
        self.assertEqual(decrypt_vigenere("", "KEY"), "")

    def test_encrypt_decrypt_key_longer_than_text(self):
        text = "HI"
        key = "LONGKEYWORD"
        encrypted = encrypt_vigenere(text, key)
        decrypted = decrypt_vigenere(encrypted, key)
        self.assertEqual(decrypted, text.upper())

    def test_encrypt_decrypt_key_shorter_than_text(self):
        text = "THISISALONGTEXT"
        key = "KEY"
        encrypted = encrypt_vigenere(text, key)
        decrypted = decrypt_vigenere(encrypted, key)
        self.assertEqual(decrypted, text.upper())

    def test_encrypt_decrypt_key_single_letter(self):
        text = "HELLO"
        key = "A"  # Shift 0
        encrypted = encrypt_vigenere(text, key)
        decrypted = decrypt_vigenere(encrypted, key)
        self.assertEqual(decrypted, text.upper())

if __name__ == '__main__':
    unittest.main()

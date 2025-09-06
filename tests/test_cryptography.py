import unittest

import app.cryptography as cryptography

class TestParser(unittest.TestCase):
    def setUp(self):
        self.test_bytes = b"test"
        self.result_encryption = cryptography.encrypt(self.test_bytes)
        self.result_decryption = cryptography.decrypt(self.result_encryption)

    def test_result_decryption(self):
        self.assertEqual(self.test_bytes, self.result_decryption)
        print(f"Test bytes: \"{self.test_bytes}\", encrypted: \"{self.result_encryption}\", decrypted: \"{self.result_decryption}\".")

if __name__ == "__main__":
    unittest.main()
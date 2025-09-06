import unittest

import app.parser as parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.test_string = "test"
        self.result_bytes = parser.to_bytes(self.test_string)
        self.result_string = parser.to_string(self.result_bytes)

    def test_result_string(self):
        self.assertEqual(self.test_string, self.result_string)
        print(f"Test string: \"{self.test_string}\", to bytes: \"{self.result_bytes}\", back to string: \"{self.result_string}\".")

if __name__ == "__main__":
    unittest.main()
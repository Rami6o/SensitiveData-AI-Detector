import unittest
import sys
import os

# patterns.py kök dizinde olduğu için parent klasörü PYTHONPATH'e ekliyoruz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import patterns



class TestRegexPatterns(unittest.TestCase):

    def test_email_pattern(self):
        pattern = patterns.EMAIL_REGEX
        self.assertIsNotNone(pattern)
        self.assertTrue(pattern.match("test@example.com"))
        self.assertFalse(pattern.match("invalid-email"))

    def test_credit_card_pattern(self):
        pattern = patterns.CC_REGEX
        self.assertIsNotNone(pattern)
        self.assertTrue(pattern.match("4111111111111111"))
        self.assertFalse(pattern.match("1234-5678-9012-3456"))

    def test_phone_pattern(self):
        self.assertTrue(patterns.PHONE_REGEX.match("05321234567"))
        self.assertTrue(patterns.PHONE_REGEX.match("+905321234567"))
        self.assertFalse(patterns.PHONE_REGEX.match("12345"))
        self.assertFalse(patterns.PHONE_REGEX.match("90532123456"))  # eksik hane

    def test_tckn_pattern(self):
        self.assertTrue(patterns.TCKN_REGEX.match("10000000146"))
        self.assertTrue(patterns.TCKN_REGEX.match("12345678901"))
        self.assertFalse(patterns.TCKN_REGEX.match("01234567890"))  # 0 ile başlayamaz
        self.assertFalse(patterns.TCKN_REGEX.match("1234567890"))   # eksik hane

    def test_iban_pattern(self):
        self.assertTrue(patterns.IBAN_REGEX.match("TR120006200119000006672315"))
        self.assertTrue(patterns.IBAN_REGEX.match("TR000000000000000000000000"))
        self.assertFalse(patterns.IBAN_REGEX.match("TR1234"))       # eksik hane
        self.assertFalse(patterns.IBAN_REGEX.match("DE89370400440532013000"))  # TR ile başlamıyor


if __name__ == "__main__":
    unittest.main()

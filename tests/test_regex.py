# tests/test_regex.py

import sys
import os
import unittest

# Kök dizini Python path'e ekle (patterns.py'yi bulabilmesi için)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import patterns  # Artık çalışmalı

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

if __name__ == "__main__":
    unittest.main()

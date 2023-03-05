from program.alternating_character import alternatingChar

import unittest

class TestAlternatingChar(unittest.TestCase):
    def test_give_AAAA_to_text(self):
        text = "AAAA"
        expected_output = 3
        result = alternatingChar(text)
        self.assertEqual(result, expected_output, f"Should return {expected_output}")
        
    def test_give_BBBBB_to_text(self):
        text = "BBBBB"
        expected_output = 4
        result = alternatingChar(text)
        self.assertEqual(result, expected_output, f"Should return {expected_output}")
        
    def test_give_ABABABAB_to_text(self):
        text = "ABABABAB"
        expected_output = 0
        result = alternatingChar(text)
        self.assertEqual(result, expected_output, f"Should return {expected_output}")

    def test_give_BABABA_to_text(self):
        text = "BABABA"
        expected_output = 0
        result = alternatingChar(text)
        self.assertEqual(result, expected_output, f"Should return {expected_output}")

    def test_give_AAABBB_to_text(self):
        text = "AAABBB"
        expected_output = 4
        result = alternatingChar(text)
        self.assertEqual(result, expected_output, f"Should return {expected_output}")
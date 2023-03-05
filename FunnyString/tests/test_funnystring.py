from FunnyString.program.funnystring import FunnyString
import unittest

class TestFunnyString(unittest.TestCase):
    def test_add_abcba_in_FunnyString(self):
        s = 'abcba'
        result = FunnyString(s)
        self.assertEqual(result, 'Funny')
        
    def test_add_aaaaa_in_FunnyString(self):
        s = 'aaaaa'
        result = FunnyString(s)
        self.assertEqual(result, 'Funny')
        
    def test_add_vwxxywv_in_FunnyString(self):
        s = 'vwxxywv'
        result = FunnyString(s)
        self.assertEqual(result, 'Funny')
        
    def test_add_pqrsqpz_in_FunnyString(self):
        s = 'pqrsqpz'
        result = FunnyString(s)
        self.assertEqual(result, 'Funny')
        
    def test__add_ivvkxq_in_FunnyString(self):
        s = 'ivvkxq'
        result = FunnyString(s)
        self.assertEqual(result,'Not Funny')
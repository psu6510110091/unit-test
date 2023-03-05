from CaesarCipher.program.caesar_cipher import caesar_Cipher
import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_add_middle_Outz_in_caesarcipher(self):
        x = 'middle-Outz'
        except_output = 'okffng-Qwvb'
        result = caesar_Cipher(x, 2)
        self.assertEqual(result,except_output)
        
    
    def test_add_abc_in_caesarcipher(self):
        x = 'abc'
        except_output = 'def'
        result = caesar_Cipher(x, 3)
        self.assertEqual(result,except_output)
        
    def test_add_hello_in_caesarcipher(self):
        x = 'hello'
        except_output = 'hello'
        result = caesar_Cipher(x, 0)
        self.assertEqual(result,except_output)
        
    def test_add_fall_in_love_in_caesacipher(self):
        x = 'fall-in-love'
        except_output = 'kfqq-ns-qtaj'
        result = caesar_Cipher(x, 5)
        self.assertEqual(result, except_output)
        
    def test_add_abcdefghijklmnopqrstuvwxyz_in_caesarcipher(self):
        x = 'abcdefghigklmnopqrstuvwxyz'
        except_output = 'defghijklmnopqrstuvwxyzabc'
        result = caesar_Cipher(x, 3)
        self.assertEqual(result, except_output)
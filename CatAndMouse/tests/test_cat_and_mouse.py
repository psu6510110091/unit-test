from CatAndMouse.program.cat_and_mouse import catAndMouse
import unittest

class TestCatAndMouse(unittest.TestCase):

    def test_cat_a(self):
        self.assertEqual(catAndMouse(1, 4, 2), "Cat A")
        self.assertEqual(catAndMouse(2, 1, 3), "Cat A")
        
    def test_cat_b(self):
        self.assertEqual(catAndMouse(1, 2, 3), "Cat B")
        self.assertEqual(catAndMouse(3, 2, 1), "Cat B")
        
    def test_mouse(self):
        self.assertEqual(catAndMouse(1, 3, 2), "Mouse C")
        self.assertEqual(catAndMouse(3, 1, 2), "Mouse C")


if __name__ == '__main__':
    unittest.main()
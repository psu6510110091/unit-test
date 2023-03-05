from program.grid_challenge import grid_challenge
import unittest

class TestGridChallenge(unittest.TestCase):
     def test_grid(self):
        grid = ['ppp','ypp','wyw']
        except_output = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, except_output)
        
     def test_grid2(self):
        grid = ['a', 'b', 'c']
        except_output = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, except_output)
        
     def test_grid3(self):
        grid = ['cba', 'fed', 'jih']
        except_output = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, except_output)
        
     def test_grid4(self):
        grid = ['hcd','awc','shm']
        except_output = 'NO'
        result = grid_challenge(grid)
        self.assertEqual(result, except_output)

     def test_grid5(self):
        grid = ['rpb','hot','qra']
        except_output = 'NO'
        result = grid_challenge(grid)
        self.assertEqual(result, except_output)
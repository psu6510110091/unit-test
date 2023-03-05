from program.staircase import Staircase
import unittest

class TestStaircase(unittest.TestCase):
    def test_give_step_negative(self):
        step = -1
        pattern = '#'
        expected_output = ''
        result = Staircase(step, pattern)
        self.assertEqual(result,expected_output)

    def test_give_step_n0(self):
        step = 0
        pattern = '#'
        expected_output = ''
        result = Staircase(step, pattern)
        self.assertEqual(result,expected_output)

    def test_give_step_n1(self):
        step = 1
        pattern = '#'
        expected_output = '#'
        result = Staircase(step, pattern)
        self.assertEqual(result, expected_output)

    def test_give_step_n15(self):
        step = 15
        pattern = '#'
        expected_output = \
            "              #\n" + \
            "             ##\n" + \
            "            ###\n" + \
            "           ####\n" + \
            "          #####\n" + \
            "         ######\n" + \
            "        #######\n" + \
            "       ########\n" + \
            "      #########\n" + \
            "     ##########\n" + \
            "    ###########\n" + \
            "   ############\n" + \
            "  #############\n" + \
            " ##############\n" + \
            "###############\n"

        result = Staircase(step, pattern)
        self.assertEqual(result, expected_output)

    def test_give_step_n40(self):
        step = 40
        pattern = '#'
        expected_output = ''
        result = Staircase(step, pattern)
        self.assertEqual(result, expected_output)
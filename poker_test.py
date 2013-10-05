import unittest
import poker
class TestPoker(unittest.TestCase):
    '''Example unittest test methods for check_rank'''
    def test_poker_example_1(self):
        '''Test check_rank poker with .'''
        actual = poker.play_poker(1)
        expected = [['1']]
        self.assertEqual(actual, expected)
    def test_poker_flush_1(self):
        '''Test Case Flush 1 '''
        actual = poker.flush(['JC', 'TC', '9C', '8C', '7C'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_flush_2(self):
        '''Test Case Flush 2 '''
        actual = poker.flush(['JD', 'TC', '9C', '8C', '7C'])
        expected = False
        self.assertEqual(actual, expected)
    def test_poker_three_of_a_kind_1(self):
        '''Test Case poker_three_of_a_kind 1 '''
        actual = poker.three_of_a_kind(['7D', '7C', '9C', '8C', '7C'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_three_of_a_kind_2(self):
        '''Test Case poker_three_of_a_kind 2 '''
        actual = poker.three_of_a_kind(['7D', '7C', '7C', '7C', '7C'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_three_of_a_kind_3(self):
        '''Test Case poker_three_of_a_kind 3 '''
        actual = poker.three_of_a_kind(['6D', '7C', '9C', '8C', '7C'])
        expected = False
        self.assertEqual(actual, expected)

     
if __name__ == '__main__':
    unittest.main(exit=False)


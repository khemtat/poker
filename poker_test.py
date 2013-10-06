import unittest
import poker
class TestPoker(unittest.TestCase):
    '''Example unittest test methods for check_rank'''
#    def test_poker_example_1(self):
#        '''Test check_rank poker with .'''
#        actual = poker.play_poker(1)
#        expected = [['1']]
#        self.assertEqual(actual, expected)

    def test_poker_royal_straight_flush(self):
        '''Test Case for checking royal straight flush'''
        actual = poker.royal_straight_flush(['AD','KD','QD','JD','TD'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_royal_straight_flush2(self):
        '''Test Case for checking royal straight flush'''
        actual = poker.royal_straight_flush(['KC','AC','JC','TC','QC'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_royal_straight_flush3(self):
        '''Test Case for checking royal straight flush'''
        actual = poker.royal_straight_flush(['KC','AD','JD','TC','QD'])
        expected = False
        self.assertEqual(actual, expected)

    def test_poker_straight_flush1(self):
        '''Test case for checking straight'''
        actual = poker.straight(['JC','KD','QD','AC','TD'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_straight_flush2(self):
        '''Test case for checking straight'''
        actual = poker.straight(['JC','KD','QD','AC','TD'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_straight_flush3(self):
        '''Test case for checking straight'''
        actual = poker.straight(['JC','KD','QD','AC','TD'])
        expected = True
        self.assertEqual(actual, expected)
        
    def test_poker_straight_1(self):
        '''Test Case straight 1 '''
        actual = poker.straight(['6H', 'TC', '9D', '8C', '7C'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_straight_2(self):
        '''Test Case straight 2 '''
        actual = poker.straight(['6H', 'TC', '9D', '8C', '2C'])
        expected = False
        self.assertEqual(actual, expected)
    def test_poker_straight(self):
        '''Test case for checking straight'''
        actual = poker.straight(['2C','3D','4D','5C','6D'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_straight2(self):
        '''Test case for checking straight'''
        actual = poker.straight(['3C','2D','5D','AC','4D'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_straight3(self):
        '''Test case for checking straight'''
        actual = poker.straight(['JC','KD','QD','AC','TD'])
        expected = True
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


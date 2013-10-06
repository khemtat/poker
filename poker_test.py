import unittest
import poker
class TestPoker(unittest.TestCase):
    '''unittest test methods for check_rank'''
#    def test_poker_example_1(self):
#        '''Test check_rank poker with .'''
#        actual = poker.play_poker(1)
#        expected = [['1']]
#        self.assertEqual(actual, expected)

    ### Test case royal straight flush ###
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

    ### Test case straight flush ###
    def test_poker_straight_flush(self):
        '''Test case for checking straight flush'''
        actual = poker.straight_flush(['AC','2C','3C','4C','5C'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_straight_flush2(self):
        '''Test case for checking straight flush'''
        actual = poker.straight_flush(['2D','3D','4C','5C','6D'])
        expected = False
        self.assertEqual(actual, expected)

    #### Test case four of a kind ###
    def test_poker_four_of_a_kind(self):
        '''Test case for checking four of a kind'''
        actual = poker.four_of_a_kind(['5D','5D','5D','5D','6D'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_four_of_a_kind2(self):
        '''Test case for checking four of a kind'''
        actual = poker.four_of_a_kind(['3C','3D','3C','3C','6D'])
        expected = True
        self.assertEqual(actual, expected) 
    def test_poker_four_of_a_kind3(self):
        '''Test case for checking four of a kind'''
        actual = poker.four_of_a_kind(['3C','3D','3C','4C','5D'])
        expected = False
        self.assertEqual(actual, expected)  

    ### Test case straight ###
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

    ### Test case flush ###
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

    ### Test case three of a kind ###
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

    ### Test case one pair ###
    def test_poker_one_pair(self):
        '''Test Case for checking one pair'''
        actual = poker.one_pair(['7D', '7C', '4C', '3C', '2C'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_one_pair2(self):
        '''Test Case for checking one pair'''
        actual = poker.one_pair(['KD', 'KC', '4C', '2C', '5C'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_one_pair3(self):
        '''Test Case for checking one pair'''
        actual = poker.one_pair(['KD', 'KC', '7C', '7C', '5C'])
        expected = False
        self.assertEqual(actual, expected)
    ### Test case two pair ###    
    def test_poker_two_pair1(self):
        '''Test case for checking two pair'''
        actual = poker.two_pair(['6D', '6C', '8C', '8C', '7C'])
        expected = True
        self.assertEqual(actual, expected)
    def test_poker_two_pair2(self):
        '''Test case for checking two pair'''
        actual = poker.two_pair(['1D', '6C', '8C', '8C', '7C'])
        expected = False
        self.assertEqual(actual, expected)
    ### Test case high card ###    
    def test_poker_high_card1(self):
        '''Test case for checking high card'''
        actual = poker.high_card(['4D', '6C', '8C', '9C', '7C'])
        expected = '9'
        self.assertEqual(actual, expected)
    def test_poker_high_card2(self):
        '''Test case for checking high card'''
        actual = poker.high_card(['KD', '6C', '8C', '8C', '7C'])
        expected = '13'
        self.assertEqual(actual, expected)
    ### Test case full house ###    
    def test_poker_full_house1(self):
        '''Test case for checking full house'''
        actual = poker.full_house(['4D', '4C', '8C', '8C', '4C'])
        expected = True
        self.assertEqual(actual, expected)
    #def test_poker_full_house2(self):
     #   '''Test case for checking full house'''
      #  actual = poker.full_house(['2D', '2C', '3C', '4C', '5C'])
      #  expected = False
     #   self.assertEqual(actual, expected)

     
if __name__ == '__main__':
    unittest.main(exit=False)


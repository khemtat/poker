def play_poker(n):
	card_list = []
	for i in xrange(n):
		card_list.append([raw_input("[+] Player "+str(i+1)+" input your card: ")])
	return card_list

def royal_straight_flush(hand):
        """
        (hand) -> bool

        Checking hand is royal straight flush

        return True or False
        """
        def royal_straight(hand):
                s1 = [s1 for s1,s2 in hand]
                for each in s1:
                        if each not in ['A','K','Q','J','T']:
                                return False
                return True
        return royal_straight(hand) and flush(hand)

def straight_flush(hand):
        """
        (hand) -> bool

        Checking hand is straight flush

        return True or False
        """
        return straight(hand) and flush(hand)

def four_of_a_kind(hand):
        """
        (hand) -> bool

        Checking hand is four of a kind

        return True or False
        """
        s = [s1 for s1,s2 in hand]
        return len(set(s)) == 2

def straight(hand):
        """
        (hand) -> bool

        return check this hand is straight
        """
        tocheck_straight = ['--23456789TJQKA'.index(n) for n,h in hand]
        tocheck_straight.sort()
        tocheck_straight.reverse()
        if tocheck_straight == [14,5,4,3,2]:
                tocheck_straight = [5,4,3,2,1]
        return (max(tocheck_straight)-min(tocheck_straight) == 4) and (len(set(tocheck_straight)) == 5)


def flush(hand):
        """
        (hand) -> bool

        return check this hand is flush
        """
        s = [h for n,h in hand]
        if len(set(s)) != 1:
                return False
        return True

def three_of_a_kind(hand):
        """
        (hand) -> bool

        return check this hand is three of a kind
        """
        s = [n for n,h in hand]
        s.sort()
        status = 0
        for i in xrange(len(s)):
                if s.count(s[i]) >= 3:
                        status = 1
                        break
        return bool(status)

def one_pair(hand):
        """
        (hand) -> bool

        Checking hand is one one pair

        return True or False
        """
        s = [s1 for s1,s2 in hand]
        return len(set(s)) == 4
def two_pair(hand):
        """
        (hand) -> bool

        return check this hand is two pair
        """
        s = [n for n,h in hand]
        if not three_of_a_kind(hand)and len(set(s))== 3:
                return True
        else:
                return False
def high_card(hand):
        """
        (hand) -> int

        return The maximum number of cards.
        """
        s=[]
        s.append('--23456789TJQKA'.index(n) for n,h in hand)
        return max(s)
def full_house(hand):
        """
        (hand) -> bool

        Checking hand is full house

        return True or False
        """
        s = [n for n,h in hand]
        if three_of_a_kind(hand)and len(set(s))==2:
                return True
if __name__ == '__main__':
	import doctest
	doctest.testmod()

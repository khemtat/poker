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
        s1, s2 = [s1 for s1,s2 in hand],[s2 for s1,s2 in hand]
        for each in s1:
                if each not in ['A','K','Q','J','T']:
                        return False
        if flush(hand):
                return True
        return False


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
        
if __name__ == '__main__':
	import doctest
	doctest.testmod()

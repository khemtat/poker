def play_poker(n):
	card_list = []
	for i in xrange(n):
		card_list.append([raw_input("[+] Player "+str(i+1)+" input your card: ")])
	return card_list
def flush(hand):
        """
        (hand) --> bool

        return check this hand is flush
        """
        s = [h for n,h in hand]
        status = 1
        for i in xrange(len(s)):
                if s[0] != s[i]:
                        status = 0
                        break
        return bool(status)
def three_of_a_kind(hand):
        """
        (hand) --> bool

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
        
if __name__ == '__main__':
	import doctest
	doctest.testmod()

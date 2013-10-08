#-*- coding:UTF-8 -*-
def main():
    print '''
   _____                                         
  /  __ \      _                                
  | /  \ \    | |
  | |__/ /___ | | _ ___  _ __
  |  ___/  _  | |/ / _ \| '__|
  | |   | (_) |   <  __/| |
  |_|    \___/|_|\_\___||_|                              
                                                
                                                  
                 ______           _           _        _____  _____  __   ___ 
                 | ___ \         (_)         | |      / __  \|  _  |/  | /   \ 
                 | |_/ /_ __ ___  _  ___  ___| |_     `' / /'| |/' |`| | \_/| | 
                 |  __/| '__/ _ \| |/ _ \/ __| __|      / /  |  /| | | |  _ < | 
                 | |   | | | (_) | |  __/ (__| |_     ./ /___\ |_/ /_| |_/ \| |
                 \_|   |_|  \___/| |\___|\___|\__|    \_____/ \___/ \___/\___/
                                _/ |                                          
                               |__/                                           
       
'''
    players = input("\n[+] Input number of players: ")
    return players
print main()

def play_poker(n):
	card_list = []
	for i in xrange(n):
		card_list.append([raw_input("[+] Player "+str(i+1)+" input your card: ")])
	return card_list

def check_hand_rank(hand):
        """
        (hand) -> list

        This function use to check hand rank

        return list of hand rank
        ======
        Royal straight flush = 9
        Straight flush = 8
        Four of a kind = 7
        Full house = 6
        Flush = 5
        Straight = 4
        Three of a kind = 3
        Two pair = 2
        One pair = 1
        High card = 0
        """
        card_rank = ['--23456789TJQKA'.index(n) for n,h in hand]
        card_rank.sort()
        card_rank.reverse()
        if card_rank == [14,5,4,3,2]:
                card_rank = [5,4,3,2,1]
        if royal_straight_flush(hand):
                return 9,max(card_rank)
        elif straight_flush(hand):
                return 8,max(card_rank)
        elif four_of_a_kind(hand):
                return 7,max(card_rank)
        elif full_house(hand):
                tong = 0
                kuu = 0
                s = [n for n,h in hand]
                for i in xrange(len(s)):
                        if(s.count(s[i])==3):
                           tong = s[i]
                        else:
                           kuu = s[i]
                return 6,int(tong),int(kuu)
        elif flush(hand):
                return 5,max(card_rank)
        elif straight(hand):
                return 4,max(card_rank)
        elif three_of_a_kind(hand):
                return 3,max(card_rank),max(kicker_sort(3,card_rank))
        elif two_pair(hand):
                max_card_rank = max(card_rank)
                Max2 = kicker_sort(2,card_rank)
                Max2_int = max(Max2)
                kicker = kicker_sort(2,Max2)
                kicker_int = max(kicker)
                return 2,max_card_rank,Max2_int,kicker_int
        elif one_pair(hand):
                return 1,max(card_rank),max(kicker_sort(2,card_rank))
        else:
                return 0,max(card_rank)
def kicker_sort(a,ls):
        """
        (a,ls) -> list

        if draw in case "Three of a kind" , "Two Pair" and "One Pair" can use
        this function to find Kicker number

        return list of kicker
        """
        b = 0
        for i in xrange(len(ls)):
                if(ls.count(ls[i]) == a ):
                        b=ls[i]
                        break
        for i in xrange(ls.count(b)):
                ls.remove(b)
        ls.sort(reverse=True)
        return ls
                        
def royal_straight_flush(hand):
        """
        (hand) -> bool

        Checking hand is royal straight flush

        return True or False
        """
        def royal_straight(hand):
                s1 = [s1 for s1,s2 in hand]
                for each in s1:
                        if each not in ['A','K','Q','J','T'] or len(set(s1)) != 5:
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
        for i in xrange(len(s)):
                if s.count(s[i]) ==4:
                        return True
        return False

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
        card_rank = ['--23456789TJQKA'.index(n) for n,h in hand]
        card_rank.sort()
        card_rank.reverse()
        if card_rank == [14,5,4,3,2]:
                card_rank = [5,4,3,2,1]
        return max(card_rank)
def full_house(hand):
        """
        (hand) -> bool

        Checking hand is full house

        return True or False
        """
        s = [n for n,h in hand]
        if three_of_a_kind(hand)and len(set(s))==2:
                return True
        else:
                return False
if __name__ == '__main__':
	import doctest
	doctest.testmod()

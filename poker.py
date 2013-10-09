#-*- coding:UTF-8 -*-
print '''
   _____                                         
  /  __ \      _                                
  | /  \ \    | |              
  | |__/ /___ | | _ ___  _ __ *
  |  ___// _ \| |/ / _ \| '__|
  | |   | (_) |   <  __/| |
  |_|    \___/|_|\_\___||_|                                                                                                            
            ______           _           _        _____  _____  __   _____ 
            | ___ \         (_)         | |      / __  \/  _  \/  | /  _  \ 
            | |_/ /_ __ ___  _  ___  ___| |_     `' / /'| |\| |`| | \_/ \ | 
            |  __/| '__/ _ \| |/ _ \/ |_  __|      / /  | |/| | | |  _ -< | 
            | |   | | | (_) | |  __/ (__| |_     ./ /___\ |_| /_| |_/ \_/ |
            \_|   |_|  \___/| |\___|\___|___|    \_____/ \___/ \___/\_____/
                            / |                                          
                           |_/
# Presented by : Kittikorn Prasertsak, Khemtat Lengpaiboon and Tanawat Gajaseni
# Enjoy the Poker game !!                                          
'''
#print main(input("\n[+] Input number of players (1-5): "))
def main(players):
    """
    (players) -> number of players in this game

    """
    Pcard = []
    i2 = 0
    while len(Pcard) < players:
        P2 = (raw_input("Player "+str(len(Pcard)+1)+" -- input your card: "))
        Pcard.append(P2.split())
        i2 += 1
    hand_rank = []
    print "==============Result=============="
    for i in xrange(players):
        hand_rank.append(check_hand_rank(Pcard[i]))
        if hand_rank[i][0] == 0:
            print "Player "+str(i+1)+" have: High card"
        elif hand_rank[i][0] == 1:
            print "Player "+str(i+1)+" have: One pair"
        elif hand_rank[i][0] == 2:
            print "Player "+str(i+1)+" have: Two pair"
        elif hand_rank[i][0] == 3:
            print "Player "+str(i+1)+" have: Three of a kind"
        elif hand_rank[i][0] == 4:
            print "Player "+str(i+1)+" have: Straight"
        elif hand_rank[i][0] == 5:
            print "Player "+str(i+1)+" have: Flush"
        elif hand_rank[i][0] == 6:
            print "Player "+str(i+1)+" have: Full house"
        elif hand_rank[i][0] == 7:
            print "Player "+str(i+1)+" have: Four of a kind"
        elif hand_rank[i][0] == 8:
            print "Player "+str(i+1)+" have: Straight flush"
        elif hand_rank[i][0] == 9:
            print "Player "+str(i+1)+" have: Royal straight flush"
    if len(str(winner(hand_rank)))/2 >= 2:
        return 'Winner are players: ' +str(winner(hand_rank))
    return "The Winner is player: " + str(winner(hand_rank))

def how_to_play():
    print '''
    Test !!
    '''

select = raw_input("[+] Select Mode [+]\n    1.)Start Game\n    2.)How to Play\n\nInput number : ")
if select.isdigit() and (select == '1' or select =='2'):
    if select == '1':
        print '==============Poker Start=============='
        print main(input("\n[+] Input number of players (1-5): "))
    else:
        print '==============How to Play=============='
        print how_to_play()
else:
    print "please nput number 1 or 2"
        
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
            ld = 0
            a = 0
            for i in xrange(0,3):
                if card_rank.count(card_rank[i]) > 1 :
                    ld = (card_rank[i])
                else:
                    a = card_rank[i]
            return 3,ld,a
        elif two_pair(hand):
            ld = []
            a = 0
            for i in xrange(0,3):
                if card_rank.count(card_rank[i]) >=2:
                    ld.append(card_rank[i])
                    card_rank.pop(i)
                else:
                    a = card_rank[i]
            ld.sort(reverse=True)
            return 2,ld[0],ld[1],a
        elif one_pair(hand):
            ld = 0
            a = []
            for i in xrange(len(card_rank)):
                if card_rank.count(card_rank[i]) > 1 :
                    ld = (card_rank[i])
                else:
                    a.append(card_rank[i])
            a.sort(reverse = True)
            return 1,ld,a[0],a[1],a[2]
        else:
                return 0,max(card_rank)

def winner(ls):
    """
    (ls) -> str

    this function use to check who win

    return Winner Player
    
    ls ex:
    [(0, 14), (1, 8, 8)]
    """
    ll = []
    maxer = 0
    value = 0
    for i in xrange(len(ls)):
        if ls[i][0] > maxer:
            maxer = ls[i][0]
            ll = []
            ll.append(i)
        elif ls[i][0] == maxer:
            maxer = ls[i][0]
            ll.append(i)
    print ll
    if len(ll) > 1:
        #High Card
        if maxer == 0:
            return max_in_case(ls,ll,1)
        #One Pair
        elif maxer == 1:
            a = max_in_case(ls,ll,1)
            if len(a) > 2:
                if a.count("1") == 0 and len(ll) > 1:
                    ll.pop(0)
                if a.count("2") == 0 and len(ll) >= 2:
                    ll.pop(1)
                if a.count("3") == 0 and len(ll) >= 3:
                    ll.pop(2)
                if a.count("4") == 0 and len(ll) >= 4:
                    ll.pop(3)
                if a.count("5") == 0 and len(ll) >= 5:
                    ll.pop(4)
                b = max_in_case(ls,ll,2,a)
                if len(b)>2:
                    c = max_in_case(ls,ll,3,b)
                    return c
                else:
                    return b
            else:
                return a
        #Two Pair
        elif maxer == 2:
            a = max_in_case(ls,ll,1)
            if len(a) > 2:
                if a.count("1") == 0:
                    ll.pop(0)
                if a.count("2") == 0:
                    ll.pop(1)
                if a.count("3") == 0:
                    ll.pop(2)
                b = max_in_case(ls,ll,2,a)
                if len(b)>2:
                    c = max_in_case(ls,ll,3,b)
                    return c
                else:
                    return b
            else:
                return a
        #Three of a kind
        elif maxer == 3:
            a = max_in_case(ls,ll,1)
            if len(a) > 2:
                if a.count("1") == 0 and len(ll) > 1:
                    ll.pop(0)
                if a.count("2") == 0 and len(ll) >= 2:
                    ll.pop(1)
                if a.count("3") == 0 and len(ll) >= 3:
                    ll.pop(2)
                if a.count("4") == 0 and len(ll) >= 4:
                    ll.pop(3)
                if a.count("5") == 0 and len(ll) >= 5:
                    ll.pop(4)
                b = max_in_case(ls,ll,2,a)
                if len(b)>2:
                    c = max_in_case(ls,ll,3,b)
                    return c
                else:
                    return b
            else:
                return a 
        #Straight
        elif maxer == 4:
            return max_in_case(ls,ll,1)
        #Flush
        elif maxer == 5:
            return max_in_case(ls,ll,1)
        #Full House
        elif maxer == 6 :
            a = max_in_case(ls,ll,1)
            if len(a) > 2:
                if a.count("1") == 0 and len(ll) > 1:
                    ll.pop(0)
                if a.count("2") == 0 and len(ll) >= 2:
                    ll.pop(1)
                if a.count("3") == 0 and len(ll) >= 3:
                    ll.pop(2)
                if a.count("4") == 0 and len(ll) >= 4:
                    ll.pop(3)
                if a.count("5") == 0 and len(ll) >= 5:
                    ll.pop(4)
                b = max_in_case(ls,ll,2,a)
                if len(b)>2:
                    c = max_in_case(ls,ll,3,b)
                    return c
                else:
                    return b
            else:
                return a 
        #Four of a kind
        elif maxer == 7:
            return max_in_case(ls,ll,1)
        #Straight Flush
        elif maxer == 8:
            return max_in_case(ls,ll,1)
        #Royal Straight Flush
        elif maxer == 9:
            return max_in_case(ls,ll,1)
    else:
        return str(ll[0]+1)

def max_in_case(ls,ll,case,old_st = ""):
    """
    max_in_case(ls,ll,case) -> str

    return who have max value of card if can to judge by hand rank
    """
    st = ""
    if old_st == "":
        if len(ll) == 2:
            a = (max(ls[ll[0]][case],ls[ll[1]][case]))
            if ls[ll[0]][case] == a:
                st += str(ll[0]+1)+" "
            if ls[ll[1]][case] == a:
                st += str(ll[1]+1)+" "
        elif len(ll) == 3:
            a = (max(ls[ll[0]][case],ls[ll[1]][case],ls[ll[2]][case]))
            if ls[ll[0]][case] == a:
                st += str(ll[0]+1)+" "
            if ls[ll[1]][case] == a:
                st += str(ll[1]+1)+" "
            if ls[ll[2]][case] == a:
                st += str(ll[2]+1)+" "
        elif len(ll) == 4:
            a = (max(ls[ll[0]][case],ls[ll[1]][case],ls[ll[2]][case],ls[ll[3]][case]))
            if ls[ll[0]][case] == a:
                st += str(ll[0]+1)+" "
            if ls[ll[1]][case] == a:
                st += str(ll[1]+1)+" "
            if ls[ll[2]][case] == a:
                st += str(ll[2]+1)+" "
            if ls[ll[3]][case] == a:
                st += str(ll[3]+1)+" "
        elif len(ll) == 5:
            a=(max(ls[ll[0]][case],ls[ll[1]][case],ls[ll[2]][case],ls[ll[3]][case],ls[ll[4]][case]))
            if ls[ll[0]][case] == a:
                st += str(ll[0]+1)+" "
            if ls[ll[1]][case] == a:
                st += str(ll[1]+1)+" "
            if ls[ll[2]][case] == a:
                st += str(ll[2]+1)+" "
            if ls[ll[3]][case] == a:
                st += str(ll[3]+1)+" "
            if ls[ll[4]][case] == a:
                st += str(ll[4]+1)+" "
        return st    
    else :
        if len(ll) == 2:
            a = (max(ls[ll[0]][case],ls[ll[1]][case]))
            if ls[ll[0]][case] == a and old_st.count(str(ll[0]+1)) != 0:
                st += str(ll[0]+1)+" "
            if ls[ll[1]][case] == a and old_st.count(str(ll[1]+1)) != 0:
                st += str(ll[1]+1)+" "
        elif len(ll) == 3:
            a = (max(ls[ll[0]][case],ls[ll[1]][case],ls[ll[2]][case]))
            if ls[ll[0]][case] == a and old_st.count(str(ll[0]+1)) != 0:
                st += str(ll[0]+1)+" "
            if ls[ll[1]][case] == a and old_st.count(str(ll[1]+1)) != 0:
                st += str(ll[1]+1)+" "
            if ls[ll[2]][case] == a and old_st.count(str(ll[2]+1)) != 0:
                st += str(ll[2]+1)+" "
        elif len(ll) == 4:
            a = (max(ls[ll[0]][case],ls[ll[1]][case],ls[ll[2]][case],ls[ll[3]][case]))
            if ls[ll[0]][case] == a and old_st.count(str(ll[0]+1)) != 0:
                st += str(ll[0]+1)+" "
            if ls[ll[1]][case] == a and old_st.count(str(ll[1]+1)) != 0:
                st += str(ll[1]+1)+" "
            if ls[ll[2]][case] == a and old_st.count(str(ll[2]+1)) != 0:
                st += str(ll[2]+1)+" "
            if ls[ll[3]][case] == a and old_st.count(str(ll[3]+1)) != 0:
                st += str(ll[3]+1)+" "
        elif len(ll) == 5:
            a=(max(ls[ll[0]][case],ls[ll[1]][case],ls[ll[2]][case],ls[ll[3]][case],ls[ll[4]][case]))
            if ls[ll[0]][case] == a and old_st.count(str(ll[0]+1)) != 0:
                st += str(ll[0]+1)+" "
            if ls[ll[1]][case] == a and old_st.count(str(ll[1]+1)) != 0:
                st += str(ll[1]+1)+" "
            if ls[ll[2]][case] == a and old_st.count(str(ll[2]+1)) != 0:
                st += str(ll[2]+1)+" "
            if ls[ll[3]][case] == a and old_st.count(str(ll[3]+1)) != 0:
                st += str(ll[3]+1)+" "
            if ls[ll[4]][case] == a and old_st.count(str(ll[4]+1)) != 0:
                st += str(ll[4]+1)+" "
        return st    
        
        
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

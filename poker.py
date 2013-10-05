def play_poker(n):
	card_list = []
	for i in xrange(n):
		card_list.append([raw_input("[+] Player "+str(i+1)+" input your card: ")])
		return card_list
if __name__ == '__main__':
	import doctest
	doctest.testmod()

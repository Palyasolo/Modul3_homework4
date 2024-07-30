def single_root_words (root_word, *other_words):
	same_words = list()
	count = 0
	for i in range (len (other_words)):
		count = other_words[i].count (root_word)
		if count > 0:
			same_words.append(other_words[i])
		count = root_word.count(other_words[i])
		if count > 0:
			same_words.append(other_words[i])
	
	print (same_words)
	
single_root_words ('as', 'daster', 'bob', 'has','a')
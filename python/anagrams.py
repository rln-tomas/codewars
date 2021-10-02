def anagrams(word, words):
	d1 = { c:word.count(c) for c in word }
	s = []
	for w in words:
		d2 = { c:w.count(c) for c in w }
		if d1 == d2: s.append(w)
	return s 
		

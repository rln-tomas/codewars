def gps(s, x): 
	if (len(x)<2): 
		return 0
	test = list()
	for i in range(len(x)-1):
		delta = x[i+1]-x[i]
		test.append(3600*delta/s)
	return max(test)

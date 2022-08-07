def persistence(num): 
	if (num < 10): 
		return 0
	else:
		num = list(str(num))
		new_num = int(num[0])
		del num[0]
		for n in num: 
			new_num *= int(n)
		return persistence(new_num) + 1

"""
Write a function, persistence, that takes in a positive parameter num and 
returns its multiplicative persistence, which is the number of times you 
must multiply the digits in num until you reach a single digit.
"""
def is_valid_IP(string):
	if (len(string.split('.')) != 4):
		return False

	for num in string.split('.'):
		if (not num.isnumeric() or not(int(num) in range(0,256)) or (len(num) > 1 and num[0] == '0')): 
			return False

	return True


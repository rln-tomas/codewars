import sys

def peelTheOnion(s,d):
	if (s==0): 
		return []
	if(s==1): 
			return [s]
	else: 
		res = s**d-(s-2)**d
		return [res] + peelTheOnion(s-2,d)		

if (len(sys.argv) < 3): 
	print('No arguments passed')
else: 
	arg1 = int(sys.argv[1])
	arg2 = int(sys.argv[2])
	print(peelTheOnion(arg1, arg2))






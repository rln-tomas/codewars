import sys


def peel_the_onion(s, d):
	if s == 0:
		return []

	if s == 1:
		return [s]
	else:
		res = s ** d - (s - 2) ** d
		return [res] + peel_the_onion(s - 2, d)


if len(sys.argv) < 3:
	print('No arguments passed')
else:
	arg1 = int(sys.argv[1])
	arg2 = int(sys.argv[2])
	print(peel_the_onion(arg1, arg2))

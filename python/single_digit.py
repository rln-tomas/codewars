import sys

def single_digit(n): 
    while (n > 9): 
        n = list(bin(n)).count('1')
    return n 

if ('__main__' == __name__): 
    n = int(sys.argv[1])
    print(single_digit(n))


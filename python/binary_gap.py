import sys
def binary_gap(num:int):
    binary = bin(num)[2:]
    res = binary.split('1')
    if binary[-1] != '1': 
        res.pop()
    return len(max(res))


if __name__ == '__main__':
    if len(sys.argv) > 1:  
        print(binary_gap(int(sys.argv[1])))


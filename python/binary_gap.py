def binary_gap(num:int):
    binary = bin(num)[2:]
    res = binary.split('1')
    return len(max(res))


print(binary_gap(1041))
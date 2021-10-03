def getDivisorsCount(num): 
    result = [ x for x in range(1, num +1) if (num % x == 0)]
    return len(result)

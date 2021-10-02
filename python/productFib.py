def productFib(number):
	fib = [0,1]
	n = 0
	while (fib[n]*fib[n+1] < number):  
			fib.append(fib[n]+fib[n+1])
			n += 1
	
	if fib[n]*fib[n+1]==number: return [fib[n], fib[n+1],True]
	return [fib[n], fib[n+1],False]
 


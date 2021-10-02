def perimeter(n):
	fib = [1,1]
	ac = 0 
	for i in range(0,n+1):
		ac += fib[i]
		fib.append(fib[i] + fib[i+1])
	return 4*ac



def row_sum_odd_numbers(n):
	initial = n**2 - (n-1)
	suma = initial
	final = 2*n+initial
	for i in range(initial+2,final, 2):
		suma = suma + i
	return suma

n = 4
print('Mi funcion: ',row_sum_odd_numbers(n))
print('Otra: ', n**3)

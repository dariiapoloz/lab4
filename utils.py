def factorial(n):
	if n < 0:
        	return
	if n == 0 or n == 1:
        	return 1
	res = n * factorial(n - 1)
return res

def factorial(n):
	if n < 0:
        	return
	if n == 0 or n == 1:
        	return 1
	res = n * factorial(n - 1)
		return res

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def is_power_of_five(n):
    if n <= 0: return False
    while n % 5 == 0:
        n //= 5
    return n == 1
def count_items(lst, i=0):
    try: lst[i]
    except: return 0
    return 1 + count_items(lst, i+1)
def sum_(lst, i=0):
    try: return lst[i] + sum_(lst, i+1)
    except: return 0

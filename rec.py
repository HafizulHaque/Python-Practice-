fact = [0] * 1001

# functions
def factorial(n):
	if n in [0,1]:
		return 1
	elif fact[n]:
		return fact[n]
	else:
		fact[n] = n*factorial(n-1)
		return fact[n]

# driver code
while(True):
	n = input("Enter a non-negetive number (-1 to exit) : ")
	n = int(n)
	if n >= 0:
		print(str(n) + "! = " + str(factorial(int(n))))
	elif n == -1:
		break
	else:
		print("Enter a valid number.")






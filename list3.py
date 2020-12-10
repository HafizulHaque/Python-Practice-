def prod(a, b, c):
	return a*b*c
arg = [2, 3, 4, 5]
print(prod(2, 3, 4))
print(prod(*arg[:-1]))
print(prod(2,*arg[1:3]))
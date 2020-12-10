def powerSum(*args, power=1):
	total = 0
	for item in args:
		total += item**power
	print(total)

if __name__ == '__main__':
	powerSum(1, 2, 3, power=2)
def calcSum(a=0, b=0):
	"""Returns summation of two number

	Both parameters are optional whose default value is 0.

	>>>calcSum()
	0
	>>>calcSum(7)
	7
	>>>calcSum(4, 5)
	9
	"""
	return a+b


def main():
	res = calcSum(7, 8)
	print(res)


if __name__ == '__main__':
	main()
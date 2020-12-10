def seriesSum(n):
	x = 1
	i = 1
	totalSum = 0
	while i <= n:
		j = 1
		tempSum = 0
		while j <= i:
			k = 1
			z = 1
			while k <= j:
				z *= x
				x += 1
				k += 1
			tempSum += z
			j += 1
		totalSum += tempSum
		i += 1
	return totalSum



inp = input("Input a integer : ")
print("Series sum is : ", seriesSum(int(inp)))
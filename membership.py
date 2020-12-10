vowels = "aeiou"

while(True):
	vowelCnt = 0
	consCount = 0
	other = 0
	str = input("Enter a string (-1 to exit) :")
	try:
		if int(str) == -1:
			print("Thank you !")
			break
	except ValueError as error:
		pass
	for char in str:
		if char.isalpha():
			if char.lower() in vowels:
				vowelCnt += 1
			else:
				consCount += 1
		else:
			other += 1
	print("Total vowel : ", vowelCnt, ", Total consonent : ", consCount, ", Others : ", other)

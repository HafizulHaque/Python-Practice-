arr = [1, 2, 3, 4, 5]
total = 0

# for arrItem in arr:
# 	total += arrItem

i = iter(arr)
while True:
	try:
		total += next(i)
	except StopIteration:
		break

print(total)
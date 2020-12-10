# for i in range(1, 100, 2):
# 	print(i)

# arr = [3, 6, 1, 0]
# sortedArr = sorted(arr)
# print(sortedArr)
# # reversedArr = reversed(arr)
# # print(reversedArr)
# for item in reversed(arr):
# 	print(item)

def calc(a, b, c, d):
	return a/b+d*c

param = [1, 2, 3, 4, 4]

print(calc(2, 3, 4, 5))
print(calc(*param))

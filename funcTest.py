arr = [1, 2, 3, 4, 5]
tup = ("cat", "dog", "pigeon")
x = 10

def func(passedArray, passedTuple, passedVariable):
	passedVariable += 10
	print("X inside function : ", passedVariable)
	passedArray.append(100)
	print("arr inside function : ", passedArray)
	passedTuple = ("bd", "aus", "eng")
	print("tuple inside function : ", passedTuple)


func(arr, tup, x)

print(x)
print(arr)
print(tup)
x = 6
arr = [5,6,7]

def change():
	x += 3
	arr[1] = 10

if __name__ == '__main__':
	change()
	print(x)
	print(arr)
x = [0, 10, 20, 30, 40]
y = []

def findItem(arr, item):
	index = 0
	while(index < len(arr)):
		if(arr[index]==item):
			break
		index += 1
	else:
		index = -1
	return index

# while clause is only executed if while condition is false or becomes false after some successive iteration of while block
# if any exception is raised in while block or break executes then else clause is skipped.

def main():
	print(findItem(y, 33))

if __name__ == '__main__':
	main()
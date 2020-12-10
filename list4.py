def deleteAll(item, list):
	pos = 0
	length = len(list)
	while(pos<length):
		if(list[pos]==item):
			list.pop(pos)
			length -= 1
		else:
			pos += 1

myList = [1, 2, 0, 1, 1, 0, 2, 3, 8, 1, 1, 1, 0, 0, 0, 3, 4, 1, 0, 1, 1]
deleteAll(1, myList)
print(myList)
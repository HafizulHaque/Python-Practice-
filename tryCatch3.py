try:
	x = 5/2
finally:
	print('no matter try block executed successfully or not it will be executed.')


def readData(fileName):
	lines = []
	f = None
	try:
		f = open('abc.txt', encoding='utf8')
		for line in f:
			lines.append(line.strip())
	except (IOError, OSError) as error:
		print(error)
		return[]
	finally:
		if f not None:
			f.close()

	return lines
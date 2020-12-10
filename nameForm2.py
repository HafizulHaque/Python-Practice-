def getFirstAndLastName():
	fNames = []
	lNames = []
	for names, fileNames in ((fNames, 'firstName.txt'), (lNames, 'lastName.txt')):
		for name in open(fileNames, encoding='utf8'):
			names.append(name.strip())
	return (fNames, lNames)

def main():
	import random
	f = open('outNames.txt', 'w', encoding='utf8');
	fNames, lNames = getFirstAndLastName()
	# fNames *= 3
	# lNames *= 3
	for fName, lName in zip(random.sample(fNames,4), random.sample(lNames,4)):
		fullName = '{} {}'.format(fName, lName)
		f.write('{}\n'.format(fullName))

if __name__ == '__main__':
	main()
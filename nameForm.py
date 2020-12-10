def getFirstAndLastName():
	fNames = []
	lNames = []
	for names, fileNames in ((fNames, 'firstName.txt'), (lNames, 'lastName.txt')):
		for name in open(fileNames, encoding='utf8'):
			names.append(name.strip())
	return (fNames, lNames)

def main():
	import random
	f = open('randomNameOutput.txt', 'w', encoding='utf8');
	fNames, lNames = getFirstAndLastName()
	for i in range(100):
		line = '{} {}'.format(random.choice(fNames), random.choice(lNames))
		f.write('{}\n'.format(line))

if __name__ == '__main__':
	main()
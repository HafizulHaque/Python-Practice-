import sys
sites = dict()

for fileName in sys.argv[1:]:
	for line in open(fileName):
		i = 0
		while True:
			site = None
			i = line.find('http://', i)
			if(i > -1):
				i += len('http://')
				for j in range(i, len(line)):
					if not(line[j].isalnum() or line[j] in '-.'):
						site = line[i:j].lower()
						break
				if(site and '.' in site):
					sites.setdefault(site, set()).add(fileName)
			else:
				break

for key in sites:
	print('{} : {}'.format(key, sites[key]))
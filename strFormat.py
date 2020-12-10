s ='Bangladesh'
t = 1971

def testFunc(s , t):
	# s = 'India'
	# t = 1947
	string = '{s} was born in {t}'.format(**locals())
	return string

print(testFunc(s, t))
import random
def randomTuple():
	p = (random.randint(-3, 3), random.randint(-3, 3))
	return p


for i in range (1,10):
	(x, y) = randomTuple()
	if x in (-2, -1, 1, 2) and y in (-2, -1, 1, 2):
		print('{} in range'.format((x,y)))
	else:
		print('{} not in range'.format((x,y)))
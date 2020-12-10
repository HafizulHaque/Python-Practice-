import random

class foundException(Exception): pass

table = ['car', 'house', 'horse']
target = 7

try:
	for recNo, record in enumerate(table):
		for rowNo, row in enumerate(record):
			for index, item in enumerate(row):
				item = random.randint(1, 10)
				if item == target:
					raise foundException()
except foundException as err:
	print('{}:{}:{}'.format(record, row, index))
else:
	print('not found the number')

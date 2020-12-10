import collections
import random
Receipt = collections.namedtuple('receipt', 'ReceiptID CustomerName ProductCount ProductPrice')

receipts = []

for _ in range (1, 6):
	r = 0
	n = ''
	for _ in range (1, 6):
		r = r*10+random.randint(1,9)
		n += random.choice('abcdefghijklmnopqrstwxyz')
	receipts.append(Receipt(r, n, random.randint(2, 10), random.randint(10, 2000)))


for item in receipts:
	print(item)

total = 0
for receipt in receipts:
	total += receipt.ProductCount*receipt.ProductPrice

print('Total sale: {}'.format(total))
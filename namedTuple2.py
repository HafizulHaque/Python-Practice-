import collections

Sales = collections.namedtuple("Sales", "productId customerId price qty")
items = []
items.append(Sales(458, 7673, 50, 5))
items.append(Sales(786, 3452, 34, 9))
total = 0
for item in items:
	total += (item.price*item.qty);
	print(item);
print('Total sell tk {}'.format(total));
# print(items[1][2]);
def change(x, y=10):
	y += 2
	return x+y

def sumAll(a, b, c, l=None):
	if l==None:
		l = []

	l.append(a)
	l.append(b)
	l.append(c)
	
	sum = 0
	for i in l:
		sum += i
	return sum

# print(change(2))
# print(change(2))

print(sumAll(1, 2, 3))
print(sumAll(1, 2, 3, [5, 6]))
print(sumAll(1, 2, 3))
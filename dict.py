d = dict(zip(('name', 'age', 'cgpa'), ('Hafiz', 34, 7.88)))

for key, value in d.items():
	print(key, ':', value)

for key in d.keys():
	print(key)

for value in d.values():
	print(value)
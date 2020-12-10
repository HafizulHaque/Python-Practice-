for i in range(5, 10):
	assert i<8, 'Error number greater than 10'
	print(i)


# python -O script.py | for disabling __debug__ mode and ignore assertion and produce error 
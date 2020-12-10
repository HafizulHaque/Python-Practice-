class CustomError(ValueError): pass

try:
	x = 5
	raise CustomError('user set')
except CustomError as err:
	print(err)

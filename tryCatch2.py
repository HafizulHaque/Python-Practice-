try:
	y = int('.9')
	x = 5/0
except: # (LookupError, ValueError):
	print('error')
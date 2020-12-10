def someFunc(d, c=9, *, a=0, b):
	return c+a+b+d

# args before * are positional, args after * are keyword arguments

def printSetup(*, size='A4', copies=2, types='colored'):
	print('{0} cop{1} of {2} printing on {3} paper'.format(copies, 'y' if copies==1 else 'ies', types, size))


if __name__ == '__main__':

	printSetup(types='black & white',size='letter')

	attr = {'copies':6, 'size':'A3'}

	printSetup(**attr)
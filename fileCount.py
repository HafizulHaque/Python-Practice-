import os
for filename in os.listdir('.'):
	print('{}:'.format(filename))
	for line in open(filename):
		print('    {}'.format(line))
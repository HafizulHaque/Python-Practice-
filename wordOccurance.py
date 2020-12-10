import sys
import os


files = [file for file in os.listdir('.') if os.path.isfile(file)] # list comprehension

for fileName in files:
	keyword = sys.argv[1]
	for lineNo, line in enumerate(open(fileName), 1):
		if keyword in line:
			print('{0}:{1}:\t{2}'.format(fileName, lineNo, line))
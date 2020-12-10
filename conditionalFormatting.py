import sys

def main():
	count = int(sys.argv[1])
	resString = "Occured {} time{}".format(count if count>0 else None, 's' if count>1 else '')
	print(resString)

if __name__ == '__main__':
	main()
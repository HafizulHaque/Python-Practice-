import sys

def fact(n):
	if n == 0:
		return 1 # base case

	return n*fact(n-1)  # recursive call


print(fact(int(sys.argv[1])))
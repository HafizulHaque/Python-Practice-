import math
import sys

def digitNeeded(N): # retruns (k, n) as k th palndrome of digit length n
	total = 0
	x = 1
	while True:
		total = 2*9*int("1"*x)
		if total >= N:
			break
		else:
			x += 1
	d = int(9*math.pow(10,x-1))
	k = total-d-N 

	if k>= 0:
		return (2*x-1, d-k)
	else:
		return (2*x, -k)

def getPalindrome(k, n):
	h = math.ceil(n/2)
	half = str(k+int(math.pow(10, h-1))-1)
	if n == 1:
		return str(k)
	elif n%2==0:
		return half+half[-1::-1]
	else:
		return half+half[-2::-1]



inp = input("Enter n : ")
res = digitNeeded(int(inp))
pal = getPalindrome(res[1], res[0])

print(str(res[1]) + " th palindrome number of length " + str(res[0]))
print("The palindrome number is : " + pal)
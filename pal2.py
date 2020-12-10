import math

def calc(x):
	return int(9*math.pow(10, x-1))
def calcSum(x):
	if x == 0:
		return -1
	else:
	 	return 18*int("1"*x)

def digitNeeded(N): # retruns (n, k) as k th palndrome of digit length n
	if 1<=N<=9:
		return (1, N)
	elif 10<=N<=18:
		return (2, N-9)
	
	x = round((-1+math.sqrt(1+4*math.log(N/18, 10)))/2)
	total = calcSum(x)
	if(total<N):
		x += 1
		total = calcSum(x)
	
	d = calc(x)
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
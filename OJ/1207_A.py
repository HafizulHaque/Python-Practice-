import math
def make(b, m, p):
	prof = 0
	b_left=b
	if b>=2*m:
		prof = p*m
		b_left = b-2*m
	else:
		prof = int(b/2)*p
		b_left = 0
	return prof, b_left

def main():
	t = int(input())
	for i in range(t):
		inp = input().split()
		b = math.floor(int(inp[0])/2)*2
		p = int(inp[1])
		f = int(inp[2])
		inp = input().split()
		h = int(inp[0])
		c = int(inp[1])
		total = 0
		if(h>c):
			total, lb = make(b,p,h)
			total += make(lb,f,c)[0]
		else:
			total, lb = make(b,f,c)
			total += make(lb,p,h)[0]
		print(total)

if __name__ == '__main__':
	main()
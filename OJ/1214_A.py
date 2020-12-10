def main():
	n = int(input())
	d = int(input())
	e = int(input())
	minRest = n
	for i in range((n//d)+1):
		for j in range((n//e)+1):
			rest = n-(i*d+j*e)
			if rest >= 0:
				minRest = min(rest, minRest)
	print(minRest)

if __name__ == '__main__':
	main()
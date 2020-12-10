def main():
	inp = input().split()
	sortedInp = sorted(inp, key=float, reverse=False)
	print(' '.join(sortedInp))

if __name__ == '__main__':
	main()
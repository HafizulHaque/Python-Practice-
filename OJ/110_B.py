def main():
	n = int(input())
	string = 'abcd'
	print(string*(n//4)+string[:n%4])

if __name__ == '__main__':
	main()
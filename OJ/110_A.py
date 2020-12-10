def main():
	cnt = 0
	
	for i in input():
		if i in '47':
			cnt += 1

	for digit in str(cnt):
		if digit not in "47":
			lucky = False
			break
	else:
		lucky = True

	if lucky:
		print('YES')
	else:
		print('NO')

if __name__ == '__main__':
	main()
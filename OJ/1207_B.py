A = []
B = []
out = []

def forms(i, j, x, y):
	if A[i][j]==1 and A[i][j+y]==1 and A[i+x][j]==1 and A[i+x][j+y]==1:
		B[i][j] = B[i][j+y] = B[i+x][j] = B[i+x][j+y] = 0
		out.append((i+x, j+y))
		return True
	else:
		return False

def ifPossible(i,j):
	ret = False
	if forms(i, j, -1, -1):
		ret = True
	if forms(i, j, -1, 1):
		ret = True
	if forms(i, j, 1, -1):
		ret = True
	if forms(i, j, 1, 1):
		ret = True
	return ret

def main():
	inp = input().split()
	n, m = (int(inp[0]), int(inp[1]))

	for i in range(n):
		t = []
		inp = input().split()
		for i in inp:
			t.append(int(i))
		A.append(t)
		B.append(t)


	for i in range(1,n-1):
		for j in range(1,m-1):
			if B[i][j] == 1:
				if ifPossible(i,j):
					continue
				else:
					print(-1)
					return
	for item in out:
		print(item[0], item[1])

if __name__ == '__main__':
	A = B = out = []
	main()
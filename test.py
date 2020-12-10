def userFunc(x):
	i = 0;
	total = 0;

	if x%2==0:
		while i<=x :
			total = total+pow(i, 2);
			i+=1;
	else:
		while i<=x :
			total = total + pow(i, 3);
			i+=1;
	return total;

n = input("Enter a integer number.. ");
ans = userFunc(int(n));
print("Your answer is : " + str(ans));	

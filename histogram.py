inp = input("Input your literal to see letter frequencies...   ")

letterFeeq = [0] * 26

for letter in inp:
	if letter.isalpha():
		letterFeeq[ord(letter.lower())-ord('a')] += 1

print("letter frequency is given bellow..")
for i in range(0, 26):
	print(chr(ord('a')+i), "  :", "#"*letterFeeq[i])
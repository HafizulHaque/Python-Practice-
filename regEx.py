import re

while True:
	exp = input()
	if exp == "-1":
		break
	pattern = "^\".*\"$"
	if re.search(pattern, exp):
		print("pattern matched")
	else:
		print("pattern not matched")
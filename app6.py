import string

skipString = string.digits+string.punctuation+"\"'"
inpString = 'a $ 500 was given to me. by a @naughty boy. i am about2move.'
pos = []
strLen = len(inpString)
for i in range(strLen):
	if inpString[i] in skipString:
		pos.append(i)
pos.sort()
for i in pos:
	inpString = inpString[:i]+' '+inpString[i+1:]

print("'{}'".format(inpString))
stritems = inpString.split()
print(stritems)
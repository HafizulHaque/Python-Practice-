def retrieveFromTag(tag, line):
	opener = "<" + tag + ">"
	closer = "</" + tag + ">"

	i = line.find(opener);

	if(i != -1):
		j = line.find(closer, i)
		i += len(opener)
		print(line[i:j])
	else:
		print("No such tag available.")


text = input("Input your line: ")
tag = input("Input tag name  : ")

retrieveFromTag(tag, text)
# f = open("file1.txt", "w+")

# for i in range(10):
# 	f.write("Hello world %d\n" %(i+1));
# f.close()


f = open("file2.txt", "r")
if f.mode=='r':
	data = f.readlines()
revisedData = ""
for line in data:
	revisedData += line[:-1]
print(revisedData)
f.close()
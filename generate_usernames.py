import sys
import collections

User = collections.namedtuple('User', 'userName firstName middleName lastName id')

ID, FIRSTNAME, MIDDLENAME, LASTNAME, DEPT = range(5)

def generateUserName(fields, userNames):
	userName = (fields[FIRSTNAME][0]+fields[MIDDLENAME][:1]+fields[LASTNAME]).replace('-', '').replace('\'', '')
	userName = originalUserName = userName[:8].lower()
	count = 1
	while(userName in userNames):
		userName = '{}{}'.format(originalUserName, count)
		count+= 1
	userNames.add(userName)
	return userName

def processLine(line, userNames):
	fields = line.split(':')
	userName = generateUserName(fields, userNames)
	user = User(userName, fields[FIRSTNAME], fields[MIDDLENAME], fields[LASTNAME], fields[ID])
	return user

def print_users(users):
	nameWidth = 32
	userNameWidth = 9

	print("{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=nameWidth, uw=userNameWidth))

	print("{0:-<{nw}} {0:-^6} {0:-<{uw}}".format("", nw=nameWidth, uw=userNameWidth))

	for key in sorted(users):
		user = users[key]
		initial = ""
		if user.middleName:
			initial = " " + user.middleName[0]

		name = "{0.lastName}, {0.firstName}{1}".format(user, initial)

		print("{0:.<{nw}} {1.id:^6} {1.userName:{uw}}".format(name, user, nw=nameWidth, uw=userNameWidth))


def main():
	if len(sys.argv)==1 or sys.argv[1] in ['--h', '--help']:
		print('Usage: {} file1 [file2 [....fileN]]'.format(sys.argv[0]))
		sys.exit()

	userNames = set()
	users = {}

	for fileName in sys.argv[1:]:
		for line in open(fileName, encoding='utf8'):
			line = line.strip()
			if line:
				user = processLine(line, userNames)
				users[(user.lastName.lower(), user.firstName.lower(), user.id)] = user
	print_users(users)

#main method
if __name__ == '__main__':
	main()

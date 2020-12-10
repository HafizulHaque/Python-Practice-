path = 'user/Hafizul haque/program files/sublime text 3.exe'
splittedList = path.split('/')
*loc, executable = splittedList
loc = '/'.join(loc)
print((loc, executable))
import sys

def isFloatEqual (a, b):
	return (a-b) < sys.float_info.epsilon


x = 2.000000000002
y = 2.000000000001

print(sys.float_info.epsilon)
print(isFloatEqual(x,y))
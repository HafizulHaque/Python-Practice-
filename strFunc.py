str = "bangladesh"


try:
	print(str.find("a", 6))
except ValueError as error:
	print("not found: " , error)
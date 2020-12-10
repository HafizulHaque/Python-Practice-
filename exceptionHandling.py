while True:
	inp = input("input an integer number(0 to exit)..  ")
	try:
		conv = int(inp)
		if not conv:
			print("Thank you.")
			break
		print("You have entered", conv, "which is an valid integer.")
	except ValueError as error:		
		print("invalid integer input.")
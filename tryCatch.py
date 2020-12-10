nums = ['78', '23', '98', 'cow', '89']
converted = []

for num in nums:
	try:
		n = int(num)
		converted.append(n)
	except ValueError as err:
		print('{} cant be converted to integer'.format(num))
	else:
		print('successfully converted {} into integer'.format(num))
	finally:
		print('{} was either successfully converted or was unsuccessful'.format(num))

# else block executed if try bolck executes without raising an error
# except block/s are executed if error occurs in try , then else block is skipped
# finally block is always executed either try block was executed successfully or not

print('\nresult\n')
for item in converted:
	print(item)


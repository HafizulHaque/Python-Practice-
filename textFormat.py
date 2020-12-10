def shorten(text, length=13, indicator='...'):
	if(len(text)>length):
		text = text[:length-len(indicator)]+indicator
	return text


names = ['Bermuda Triangle', 'Bangladesh', 'Pakistan', 'Spance Harbour', 'Antigua and Montinegro', 'California']

for name in names:
	print(shorten(name))
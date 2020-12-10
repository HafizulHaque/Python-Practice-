import sys
import string

string = string.punctuation + string.digits + string.whitespace + "\"'"

wordsDict = dict()

for fileName in sys.argv[1:]:
	for line in open(fileName):
		for word in line.lower().split():
			word = word.strip(string)
			if word:
				wordsDict[word] = wordsDict.get(word, 0) + 1

for word in sorted(wordsDict):
	print("'{}' occurs {} time/s".format(word, wordsDict[word]))

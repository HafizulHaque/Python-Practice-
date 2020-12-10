import sys

Language = 'en'

ENGLISH = {0: 'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
BANGLA  = {0: 'Sunno', 1:'Ek', 2:'Dui', 3:'Tin', 4:'Char', 5:'Panch', 6:'Choy', 7:'Sat', 8:'Ath', 9:'Noy'}

def printDigits(digits):
	f = open('outputDigit.txt', 'w', encoding='utf8')
	dictionary = ENGLISH if Language=='en' else BANGLA
	for digit in digits:
		print(dictionary[int(digit)], end=' ', file=f)
	print(file=f)
	f.close()

def main():
	if len(sys.argv)==1 or sys.argv[1] in ['-h', '-help']:
		print('Usage: {0} [en|bn] number'.format(sys.argv[0].strip()))
		sys.exit()

	args = [arg.strip() for arg in sys.argv[1:]]

	if args[0] in {'en', 'bn'}:
		global Language
		Language = args.pop(0)
	printDigits(args.pop(0))

# if you want to change the value of a global Variable in a local function you have declare it as global in local function

if __name__ == '__main__':
	main()
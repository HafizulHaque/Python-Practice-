import sys
import collections
import math

Statistics = collections.namedtuple('Statistics', 'count mean median mode std')

def readData(fileName,numbers, frequency):
	for lineNo, line in enumerate(open(fileName, encoding='utf8'), start=1):
		for num in line.split():
			try:
				n = float(num)
				numbers.append(n)
				frequency[n] += 1
			except ValueError as err:
				print("FILE:{fileName},LINE NO:{lineNo}:: skipping {num} - {err}".format(**locals()))

def medianCalc(numbers):
	numbers = sorted(numbers)
	l = len(numbers)
	med = numbers[l//2]
	if (l%2==0):
		med = (med + numbers[l//2-1])/2
	return med

def modeCalc(frequency, maxModeCnt):
	heighstFreq = max(frequency.values())
	nums = [k for k,v in frequency.items() if v == heighstFreq]
	if 1 <= len(nums) <= maxModeCnt:
		return nums
	else:
		return None

def stdCalc(numbers, mean):
	total = 0
	for num in numbers:
		total += (num-mean)**2
	return math.sqrt(total/len(numbers))

def calculateStatistics(numbers, frequency):
	numCount = len(numbers)
	mean = sum(numbers)/numCount
	median = medianCalc(numbers)
	mode = modeCalc(frequency, 3)
	std = stdCalc(numbers, mean)

	stat = Statistics(numCount, mean, median, mode, std)
	return stat

def printResult(statistics):
	print('\n{0:.<{nw}}'.format("", nw='40'))
	print('{0:^40}'.format("RESULT"))
	print('{0:.<{nw}}'.format("", nw='40'))
	print('{0:20}:{1}'.format('Number Count', statistics.count))
	print('{0:20}:{1}'.format('Mean', statistics.mean))
	print('{0:20}:{1}'.format('Median', statistics.median))
	print('{0:20}:{1}'.format('Mode', statistics.mode))
	print('{0:20}:{1}'.format('Standard Deviation', statistics.std))

def main():
	if len(sys.argv)==1 or sys.argv[1] in ['--h', '--help']:
		print('Usage: {} file1 [file2 [....fileN]]'.format(sys.argv[0]))
		sys.exit()

	numbers = []
	frequency = collections.defaultdict(int)

	for fileName in sys.argv[1:]:
		readData(fileName, numbers, frequency)

	if numbers:
		statistics = calculateStatistics(numbers, frequency)
		printResult(statistics)
	else:
		print("No data found")

if __name__ == '__main__':
	main()
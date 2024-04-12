import time

def timeType(wVa):
	startTime = time.time()
	x = input('go: ')
	endTime = time.time()
	elapsedTime = endTime - startTime
	xSplit = x.split(' ')
	wpm = (len(xSplit) / elapsedTime) * 60
	cpm = (len(x) / elapsedTime) * 60
	print('Word splt. WPM:', wpm)
	xSplit = len(x) / 6.1
	wpm = (xSplit / elapsedTime) * 60
	print('Word avrg. WPM:', wpm)
	print('Char splt. CPM:', cpm)
	print('Elapsed time:', elapsedTime)
	print('Number of Words:', len(x.split(' ')))
	print('Number of Characters:', len(x))

timeType(0)

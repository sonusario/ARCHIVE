def binToDec(arr):
	arrLen = len(arr)
	maxVal = (2**arrLen) / 2
	total = 0
	for i in arr:
		total += maxVal * i
		maxVal /= 2
	return int(total)

print(binToDec(list(int(j) for j in(i for i in input('Enter binary number: ')))))

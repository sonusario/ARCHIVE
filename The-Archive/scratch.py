x = 21
print(x)
x = "hi"
print(x)
x = "25"
b = 4
print(x + str(b))
x = 25
print(x + b)
'''
>>> d = [0, 1, -1, 1, -1, 0, -1, 0, 1, 1, -1, 0, -1, 0, 1, 0, 1, -1, -1, 0, 1, 0, 1, -1, 1, -1, 0]
>>> f = [-1, -1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1]
>>> g = [[[0, 1, -1], [1, -1, 0], [-1, 0, 1]], [[1, -1, 0], [-1, 0, 1], [0, 1, -1]], [[-1, 0, 1], [0, 1, -1], [1, -1, 0]]]
>>> h = [[[-1, -1, 0], [-1, 0, 0], [0, 0, 0]], [[-1, 0, 0], [0, 0, 0], [0, 0, 1]], [[0, 0, 0], [0, 0, 1], [0, 1, 1]]]
>>> def foAdd(arr):
	add = arr[0] + arr[1] + arr[2]
	carry = int(add/2)
	out = add + (3*-carry)
	return carry,out

>>> def fpAdd(arr):
	index = triToDec(arr) + 13
	return f[index],d[index]

>>> def fnAdd(arr):
	i = arr[0] + 1
	j = arr[1] + 1
	k = arr[2] + 1
	return h[i][j][k],g[i][j][k]

>>> def fTestAdds(n,arr):
	startTime = time.time()
	for i in range(n):
		x = foAdd(arr)
	print('oAdd completed in',time.time() - startTime,'seconds.')
	startTime = time.time()
	for i in range(n):
		y = fpAdd(arr)
	print('pAdd completed in',time.time() - startTime,'seconds.')
	#y = 'NA'
	startTime = time.time()
	for i in range(n):
		z = fnAdd(arr)
	print('nAdd completed in',time.time() - startTime,'seconds.')
	return x,y,z

'''

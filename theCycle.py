def cycle(arr):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] == 0:
            arr[d] = 1
            return list(arr)
        else:
            arr[d] = 0
        d -= 1

    return list(arr)

print(cycle(list(int(j) for j in(i for i in input('Enter binary number: ')))))

def triCycle(arr, direction):
    d = len(arr) - 1

    while d >= 0:
        if arr[d] < 1:
            arr[d] += direction
            return list(arr)
        else:
            arr[d] = -1
        d -= 1

    return list(arr)

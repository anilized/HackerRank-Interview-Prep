def minimumSwaps(arr):
    numSwaps = 0
    i = 0
    while(i < len(arr)-1):
        if arr[i] != i+1:
            tmp = arr[i]
            arr[i], arr[tmp-1] = arr[tmp-1], arr[i]
            numSwaps += 1
        else:
            i += 1
    return numSwaps

print(minimumSwaps([4, 3, 1, 2]))
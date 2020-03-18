def hourglassSum(arr):

    max1 = arr[0][0] + arr[0][1] + arr[0][2] 
    max2 = arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2]
    maximum = max1 + max2

    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            if (arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2] > maximum):
                maximum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]

    return maximum
# 2 shif operation to left [1,2,3,4,5]
# -> [3,4,5,1,2]

def rotLeft(a, d):
    return a[d:]+a[:d]



a = [1,2,3,4,5]
d = 4
print(rotLeft(a,d))

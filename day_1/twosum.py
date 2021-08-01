def twosum( num, target):
    for i in range(0,len(num)):
        for j in range(i+1, len(num)):
            if(num[i]+num[j] == target):
                return [i,j]
arr = [1,2,3,4]
target = 3
x = twosum(arr, target)
print(x)   
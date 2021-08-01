def twosumOpti( num, target):
    dic = dict()
    for i in range(0,len(num)):
        dic[num[i]] = i
    for i in range(0,len(num)):
        x = target - num[i]
        if x in dic:
            return[i, dic[x]]

    
arr = [1,2,3,4]
target = 3
x = twosumOpti(arr, target)
print(x)   
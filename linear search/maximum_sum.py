n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse = True)
if arr[0]<0:
    print(arr[0],1)
else:
    i = 0
    s = 0
    l = len(arr)
    while(i<l and arr[i]>=0):
        s+=arr[i]
        i+=1
    print(s,i)
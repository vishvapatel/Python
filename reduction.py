n=int(input())
k=int(input())
arr=[int(i) for i in input().split()]
i=0
list.sort(arr)
while ( min(arr[i],arr[i+1]) > k and i < n):
    arr[i]= arr[i]-1
    arr[i+1] = arr[i] - 1
    i=i+1
else:
    print(sum(arr))

def com_sorting(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[j]
        while j>=0 and key < arr[j]:
             arr[j+1]=arr[j]
             j=j-1
        arr[j+1]=key

arr = [1,2,5,0,8,5]
com_sorting(arr)
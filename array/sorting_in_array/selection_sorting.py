def selection_sorting(arr):
    for x in range(len(arr)-1):
        # print(x)
        min_ind = x
        for j in range(x+1,len(arr)):
            if arr[min_ind]>arr[j]:
                min_ind=j
                # print(min_ind)
        arr[x], arr[min_ind] = arr[min_ind], arr[x]
    print ("Sorted array")
    for x in range(len(arr)):
        print(arr[x],end=" ") 
        # i=arr[0]
        # print(arr[x])
        



arr = [2,1,5,9,3,1]
selection_sorting(arr=arr)
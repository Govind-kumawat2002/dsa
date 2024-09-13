def binary_search(arr, search,i ,j ):
    while i <=j:
        mid=i+(j-1)//2
        if arr[mid]==search:
            return mid
        elif arr[mid]>search:
            return binary_search(arr=arr,i=mid+1,j=j,search=search)
        else:
            return binary_search(arr=arr,i=i ,j=mid-1,search=search)
    return -1 # that is edicate the , the element is not present in array 
arr = [1,2,3,4,5,6,7,8,89]
i =0
j = len(arr)-1
print(binary_search(arr,search=8,i=i,j=j))
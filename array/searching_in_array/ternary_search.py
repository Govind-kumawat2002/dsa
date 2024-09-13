# ternary search 
# role of sorted list / array
# hm ese 3  part me todenge 
def ternary_search(arr, i , j , target ):
    
    while i<=j:
        
        mid =i +(i-j)//3
        mid1 = j - (j-i)//3
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid1]==target:
            return arr[mid1]
        elif target > arr[mid]:
            return ternary_search(arr, i, j= mid+1,target=target)
        elif target<arr[mid1] :
            return ternary_search(arr=arr, i=mid-1, j=j , target=target)
        else:
            return ternary_search(arr=arr, i = mid+1, j= mid1+1, target=target)
    return -1





    # if arr[mid]==target or arr[mid1]==target:
    #     return arr[mid] or arr[mid1]
    # elif arr[mid]>target or arr[mid1]>target:
    #     return ternary_search(arr i , j= mid-1 or mid1-1, target )
arr = [1,2,3,4,5,6,7,8,9,11,12,13,14]
i = 0 
j = len(arr)-1
target = 11
reult =ternary_search(arr, i , j , target)
print(reult)
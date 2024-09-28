# def sorting(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i-1
#         while j>=0 and key <arr[j]:
#             arr[j+1]=arr[j]
#             j = j-1
#         arr[j+1]=key
#     return arr


# arr = [4,3,5,1,2]

# result=sorting(arr=arr)
# print("result ",result)


def sorting(arr):
    # comparision sorting 
    # i and j 
    # i == starting point 1 se start  and j is  0 point 
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1 
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return  arr
        

    

arr = [1,2,8,5,5]
sorting(arr)
# largest element in a array
# def largest(arr):
#     larget_e =arr[0]
#     for x in range(1, len(arr)):
#         if arr[x]>la:

#             larget_e=arr[x]
#     return larget_e


# arr = [1,2,3,4,5]

# largest(arr)

# def largest(arr):
#     max = arr[0]
#     for i in range(max+1,len(arr)):
#         if arr[i]>max:
#             max = arr[i]
#     return max
#     # pass
# arr = [4,5,2,8,4,9]
# result =largest(arr)
# print("the maximun element in array ",result)



# second largest number in a array :
# def second_largest(arr):
#     largest = -1
#     second_max = -1
#     for i in arr:
#         if i>largest:
#             second_max =largest
#             largest = i  

#     return second_max         

# arr = [1,2,5,58]
# print(second_largest(arr))

# def sorted_array(arr):
#     for x in range(len(arr)-1):
#         if arr[x]>arr[x+1]:
#             return False
#     return True


# arr = [1,2,3,4,5,0]
# print(sorted_array(arr))
# remove element form sorted array 
# def remove_element(arr):
#     duplicate=None
#     for x in arr:
#         if x==x:
#             duplicate=x
#             if duplicate==arr[x]:
#                 return"present hai ",duplicate

        
#     return duplicate

# arr = [1,2,3,4,4,5,6]
# print(remove_element(arr))
# def remove_element(arr):
#     k = 1 
#     for i in range(1, len(arr)):
#         if arr[i]!=arr[k-1]:
#             arr[k]=arr[i]
#             k+=1
#     return k

# arr = [1,1,2,2,3,3]
# print(remove_element(arr))


# Rotated array in python 
# def Rotate_array(arr,k ):
#     # for x in range(len(arr)):
        
#     a=arr[1:k]
#     b=arr[k:]
#     return b+a
            

# k = 3 
# arr = [1,2,3,4,5,6,7]
# print(Rotate_array(arr,k))


# def move_zeros(arr):
    
# print(move_zeros(arr))


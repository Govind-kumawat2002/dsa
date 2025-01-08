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

# linear- search in array
# def liner_search(arr ,element):
#     for i in range(len(arr)):
#         if arr[i]==element:
#             return i 

# arr = [1,2,3,4,5]
# element = 5 
# print(liner_search(arr,element))

# binary searching 
# def binary_search(arr, target):
    
#   q = arr[0]
#   p = len(arr) - 1
#   mid =(p+q)//2
#   for i in range(len(arr)):
#     if arr[mid]==tagert:
#         return i 
#     elif arr[mid]<tagert:
#         q=mid+1
#     elif arr[mid]>tagert:
#         p = mid-1
        

# arr = [ 1,2,3,4,5,6]
# tagert = 3 
# print(binary_search(arr, tagert))




### find the union from a array 
# def union_array(arr1,arr2):
#     set_array1 = set(arr1)
#     set_array2 = set(arr2)
#     result =set_array1.union(set_array2)
#     return list(result)
# arr1 =[1,2,3,4,5,6,7]
# arr2 = [1,2,3,4,6,7,7] 
# print(union_array(arr1,arr2))




# missing number in array 


# def missing_number(arr):
#     for x in range(0,(len(arr)+1)):
#          if x !=arr[x]:
#             return x 
# arr = [0,1,2,3,5,6,7]
# print(missing_number(arr))
 






# max consecutive ones
# def max_one(nums):
#     current = 0
#     max_y = 0
#     for x in nums:
#         if x==1:
#             current+=1
#             max_y=max(current ,max_y)
#         else:
#             current =0
#     return max_y

# nums = [1,1,2,0,1,1,1]
# print(max_one(nums))


# find the single value in array 
def single_element(num):
    duplicated = []
    sinle =[]
    for x in range(len(num)):
        for y in range(x+1,len(num)):
            if num[x]==num[y]:
                duplicated.append(num[y])
            else:
                sinle.append(num[x])

    return sinle



num = [1,1,0,2,2,3,3]
print(single_element(num))
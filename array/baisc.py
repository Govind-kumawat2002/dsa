# searching in array 

# def search(arr, element ):
#     for x in range(len(arr)):
#         # print(x)
#         if arr[x]==element:
#             return x 
#     return "this element is not present " 
     


# arr  = [1,2,3,54,2,58,2]
# result =search(arr,element = 2 )
# print("the element postion is ",result)



# two element sum 
# class Twosum:

#     def twosum(arr , target ):
#         for x in range(len(arr)):
#             for y in range(x+1,len(arr)):
#                 if arr[x]+arr[y]==target:
#                     return[x,y ]
#         return None
    
#     result=twosum()
#     print("two number sum in array ", result)

# sum=Twosum()
# print(sum.twosum(arr = [1,2,3,54,58],target=55))



# how to get the middle value of two sum array 
# Median of Two Sorted Arrays
# def median(arr, arr1):
#     arr=arr+arr1
#     median = (len(arr)+1)/2
#     return median

# arr = [1,2]
# arr1 = [3]
# result =median(arr, arr1)
# print("the result is ",result)

# 3 sum in array 
# def sum_3(arr, target ):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             for k in range(j+1,len(arr)):
#                 if arr[i ]+arr[j]+arr[k]==target:
#                     return [i , j , k ]
#     return "the sum is not posible ", arr,"because the number is differents "
   
# arr = [ 1,-1,1]
# target = 0 
# result =sum_3(arr , target)
# print("the 3 sum is ",result)
# def Sum3_Closest(arr, target ):

#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i 
#         for j in range(i+1 , len(arr)):
#             if arr[j]==target:
#                 return j 
#             for k in range(j+1, len(arr)):
#                 return k 
#             return [arr[i] , arr[j] , arr[k] ]

# arr =[-1,2,1,-4]
# target = -4 
# result =Sum3_Closest(arr, target)
# print(result)


#  Remove Duplicates from Sorted Array
# def dupliacates(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i]==arr[j]:
#                 del arr[i]

#         #    return arr[i]
            
#     return -1 


    
# arr = [1,2,3,4,3]
# result =dupliacates(arr)
# print("the duplicates value in array ",result)



# remove element form a sorted list 
# def removes(arr, key ):
#     for x in arr:
#         if arr[x] == key:
#             del arr[x]
#             return arr

#     return "out of range "


# arr = [1,2,3,4,5]
# key  = 4
# result =removes(arr,key)
# print(result)


# Next Permutation

# def permulation(arr):
#    return arr[::-1]
#     # array = [ x,y,x]
#     # for i in range(len(arr)):
#         # for j in range(i+1, len(arr)):
#         #     for k in range(j+1, len(arr)):
#                 # # print(arr[i]==arr[j])
#                 # # arr[k]=arr[i]
#                 # # arr[j]=arr[k]
#                 # if arr[i]!=arr[j]:
#                 #     arr[i]=arr[j]
#                 # elif arr[j]!=arr[k]:
#                 #     return arr[j]==arr[k]
#                 # elif arr[k]!=arr[i]:
#                 #    return arr[k]==arr[i]



# arr = [1,2,3] 
# result =permulation(arr)
# print(result)


# Search in Rotated Sorted Array
# def searching_in_sorted_array(arr,target ):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1
    


# arr = [1,2,3,5,4]
# result =searching_in_sorted_array(arr, target = 5)
# print(result)


# Find First and Last Position of Element in Sorted Array

# def find_first(arr ,target ):

#     for i in range(len(arr)):
        
#         for j in range(i+1,len(arr)):
#            if arr[i]==arr[j]:
#                 if arr[i]==target:
#                     return [i ,j ]
#     return [-1,-1]
                    

    
# arr = [1,5,5,8,8]
# result =find_first(arr, target = 8 )
# print(result)

# Search Insert Position

# def search_insert_position(arr,target):
#     for x in range(len(arr)):
#         if arr[x]==target:
#             return "that is already present in array",x
        

            
        

        
        

    
# arr = [1,3,4,5]
# result=search_insert_position(arr,target = 2)
# print(result)
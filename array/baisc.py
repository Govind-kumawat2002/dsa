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
def dupliacates(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]:
                del arr[i]

        #    return arr[i]
            
    return -1 


    
arr = [1,2,3,4,3]
result =dupliacates(arr)
print("the duplicates value in array ",result)
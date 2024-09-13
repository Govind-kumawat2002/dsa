# import math
# infinity = math.inf
# # print(infinity)
# def binary_search(arr,i , j , x):

#     # for x in range(len(arr)-1):
#     mid = i +(j-1)//2
#     if arr[mid]==x:
#         return mid
#     elif arr[mid]>x:
#         return binary_search(arr=arr, i=mid+1,j= j, x=x )
#     else:
#         return binary_search(arr=arr, i = mid-1, j=j, x=x)
# arr = [1,5,21,5,52,5,5852,infinity,infinity,infinity]
# i = 0
# j = len(arr)-1
# x = infinity

# result =binary_search(arr, x=infinity,i=i,j=j)
# print("index of this element",result)



def twosum(arr, target):
        for y in arr:
            for x in range(len(arr)):
                if arr[y]+arr[x]==target:
                        return arr

arr = [12,54,5,4,5]
target = 9
twosum(arr, target)
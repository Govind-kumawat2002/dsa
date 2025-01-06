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

def sorted_array(arr):
    for x in range(len(arr)-1):
        if arr[x]>arr[x+1]:
            return False
    return True


arr = [1,2,3,4,5,0]
print(sorted_array(arr))
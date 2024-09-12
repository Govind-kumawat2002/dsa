# arr = [1,5,5,55]
# # print(arr[1])  # index number 
# # search for an element 
# # print(77 in arr) # present in element in array 
# arr = [1,5,5,55]
# # linear Search 



# class Hello:
#     def plus()
# x=Hello()
# name = " Govind"
# print("My name is ",name)
# k=gd..
# GS VO SHBHO THIS
# >>>>>>>>>>>>>>>>>>>searching element in array<<<<<<<<<<<<<
# def linearsearch(arr,x):
#     for y in range(len(arr)):
#         if arr[y]==x:
#             return y
#         # else:
#     # return 

# arr = [1,2,3,5,6,6,1,6,41,6,1]

# result=linearsearch(arr=arr,x=3)
# print("that is present inside the array",result)


# >>>>>>>>>>>>>>>>>>>insert element any positiuoin in array>>>>>>>>>>>>>>>>>>>>>
# def insert(arr, position ,data):
#     a = []
#     for x in range(len(arr)):
#         if arr[x]==position:
#             arr[position]=data

            
    

# arr = [ 1,2,5,52,5,52,5,5,20]

# result=insert(arr=arr,position=2,data = 12)
# print("Insert position at location ",arr)



# <<<<<<<<<<<<<<<<<<<<<Remove element any position >>>>>>>>>>>>>>>>>>


# def Remove(arr,index):
#     for x in range(len(arr)):
#         if x<index:
#          del arr[index]
# arr =[1,2,5,52,5,52,5,5,20]
# Remove(arr=arr,index=2)
# print(len(arr))
# def Remove(arr, index):
#     if index < len(arr):  # Ensure index is valid
#         del arr[index]  # Remove the element at the specified index

# arr = [1, 2, 5, 52, 5, 52, 5, 5, 20]
# Remove(arr=arr, index=2)
# print(arr)  # Output: 8

# def Remove(arr , index):
#     for x in range(len(arr)):
#         if x==index:
#             del arr[index]

# arr = [1, 2, 5, 52, 5, 52, 5, 5, 20]
# Remove(arr, index=2)
# print(arr)



# <<<<<<<how to work of a len functiuon in python<<<<<<

# def len(arr):
#     count = 0
#     for x in arr:
#         count +=1

#     # return count
#     print(count)
# arr = [ 1,2,5,5,5,58,41,6,4]
# len(arr)

# def count(arr, count ):
#     y =0
#     for x in arr:
#         if x==count:
#             y+=1
#     print(y)
# arr = [2,5,8,5,8,5,2,5,2]    
# count(arr,count=88)


# >>>>>crete pop funtion in python <<<<<<<<<<
# def pop(arr):
#     # for x in range(len(arr)):
#         del arr[-1]
        




# # print(arr)
# arr = [2,5,8,5,8,5,2,5,2] 
# pop(arr)
# print(arr)

# >>>>>>>shorting in array<<<<<<<<<
# def short(arr):
#     for x in arr:
#         # print(x)


# arr =[2,5,8,5,8,5,2,5,2] 
# short(arr)


# >>>>>>>find the indexing value in data struture
# def index(arr, position):
#     count = 0
#     for x in arr:
#         count+=1
#         if count==position:
#             print(x)
# arr = [2,5,8,5,8,5,2,5,2]

# index(arr , position=5)
# print("djhbbd")

# >>>>>>>Reverse<<<<<
# def reverse(arr):
#     a=arr[::-1]
#     print(a)
    

# arr= [1,2,54,2,5,52,35,2,5]
# reverse(arr)


# def insertion_sort(arr):
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# # Example usage
# my_list = [12, 11, 13, 5, 6]
# insertion_sort(my_list)
# print(my_list)  # Output: [5, 6, 11, 12, 13]




# >>>>>>binary search array>>>>>>>>>>>>>>

# def binary_search(arr, item ):
#     #  for x in range(len(arr)/2):
#         #   print(x)
#         for x in range(len(arr)):
#                 # print(arr[0]+arr[len(arr)]% 2==0)
     
#     # for x in range(len(arr)):
        

    

# arr = [1,2,3,4,5,6,7,8,9]
# binary_search(arr, item = 8)

# dt={'battery':0,'biological':1,'brown-glass':2,'cardboard':3,'clothes':4,'green-glass':5,'metal':6,'paper':7,'plastic':8,'shoes':9,'trash':10,'white-glass':11}
# y = []
# for label in labels:
#     y.append(dt[label])







# >>>>>>>>>>>>>>>>>>>>>>>>>binary search in array>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def binary_search(arr, search_element):
    # haf=(arr[0]+len(arr))//2
    # print(haf)
        mid=(arr[0]+len(arr))//2
        if arr[mid]==search_element:
                print(arr[search_element])

        elif arr[mid]>search_element:
                 print(arr[search_element])
                
                # print(search_element)
        elif arr[mid]<search_element:
                # print(arr[search_element])
                print(arr[search_element])
                
        else:
                print("that is not mid position ")
        # print(arr[mid])
                
                
        # for mid in arr:
                
         

arr = [1,2,5,6,7,8,9,10,11,12,13,14]
binary_search(arr, search_element=10)
        

    
        

    
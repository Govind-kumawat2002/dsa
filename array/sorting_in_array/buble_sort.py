
# def buble_sort(a, i ,j ):   
#     for i in range(len(a)):
#         for x in range(0,i-x-1):
#             if a[i]>a[x] or  a[i]<a[x]:
#                 # return buble_sort(a) 
#                 pass





# a = [1,2,8,2,58,5,81]
# i = 0
# j = i+1
# result=buble_sort(a , i , j )
# print(result)
def buble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

    


a = [2,3,5,8,40,1]
result =buble_sort(a=a)
print("apply the bubble sort ",result)


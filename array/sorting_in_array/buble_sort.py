
def buble_sort(a, i ,j ):   
    for i in range(len(a)):
        for x in range(0,i-x-1):
            if a[i]>a[x] or  a[i]<a[x]:
                # return buble_sort(a) 
                pass





a = [1,2,8,2,58,5,81]
i = 0
j = i+1
result=buble_sort(a , i , j )
print(result)
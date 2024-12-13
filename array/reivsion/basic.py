# import time 
# start =time.time()
# print(1+5+6)
# print(time.time()-start)
# import sys   # 
# lst = []
# lst.append(13)
# lst.append(11)

# print(sys.getsizeof(lst))
# print(lst)
# lst = [ ]
# for x in range(100):
#     print(x,sys.getsizeof(lst))
#     lst.app
# import ctypes # create a datatype byusing ctypes 
# class Meralist:
#     def __init__(self):
#         self.size = 1   # kite item story kr skte ho 
#         self.n = 0  # kite item store hai 
#         self.A=self.create_array(self.size)
#     def create_array(self,capacity):
#         # create a c ype array statics , referential 
#         return (capacity*ctypes.py_object)()
    

# lst =Meralist()
# print(type(lst))

# len function 
# import ctypes # create a datatype byusing ctypes 
# class Meralist:
#     def __init__(self):
#         self.size = 1   # kite item story kr skte ho 
#         self.n = 0  # kite item store hai 
#         self.A=self.create_array(self.size)


#     def __len__(self):
#         return self.n
#     def create_array(self,capacity):
#         # create a c ype array statics , referential 
#         return (capacity*ctypes.py_object)()
    

# lst =Meralist()
# print(type(lst))
# print(len(lst))


### append #### 
# import ctypes # create a datatype byusing ctypes 
# class Meralist:
#     def __init__(self):
#         self.size = 1   # kite item story kr skte ho 
#         self.n = 0  # kite item store hai 
#         self.A=self.create_array(self.size)


#     def __len__(self):
#         return self.n
    
#     def __append__(self,item):
#         if self.n ==self.size:
#             return self.__resize(self.size*2)
#         self.A[self.n]=item
#         self.n = self.n +1 
             
#     def __resize(self,new_capacity):
#         B=self.create_array(new_capacity)
#         self.size = new_capacity
#         for x in range(self.n):
#             B[x]= self.A[x] 
#         self.A=B

#     def create_array(self,capacity):
#         # create a c ype array statics , referential 
#         return (capacity*ctypes.py_object)()
    

# lst =Meralist()
# lst.__append__(2)
# lst.__append__(2)
# lst.__append__(7)
# print(len(lst))


##### print 

# import ctypes # create a datatype byusing ctypes 
# class Meralist:
#     def __init__(self):
#         self.size = 1   # kite item story kr skte ho 
#         self.n = 0  # kite item store hai 
#         self.A=self.create_array(self.size)


#     def __len__(self):
#         return self.n
    
#     def __append__(self,item):
#         if self.n ==self.size:
#             return self.__resize(self.size*2)
#         self.A[self.n]=item
#         self.n = self.n +1 


#     def __str__(self):
#         result = ""
#         for x in range(self.n):
#             result = result +str(self.A[x]) + ','
            
#         return '['+result+']'
#     def __getitem__(self , index):
#         if 0<index<self.n:


#             return self.A[index]
#         else :
#             return 'out of range '

             
#     def __resize(self,new_capacity):
#         B=self.create_array(new_capacity)
#         self.size = new_capacity
#         for x in range(self.n):
#             B[x]= self.A[x] 
#         self.A=B

#     def create_array(self,capacity):
#         # create a c ype array statics , referential 
#         return (capacity*ctypes.py_object)()
    

# lst =Meralist()
# lst.__append__(22)
# lst.__append__(23)
# lst.__append__(7)
# lst.__append__("hello")
# lst.__append__("hello")
# lst.__append__("hiii")
# lst.__append__("ram ram sa ")
# lst.__append__("jai  shree ram ")

# # print(len(lst))
# print(lst[2])



# index

# import ctypes # create a datatype byusing ctypes 
# class Meralist:
#     def __init__(self):
#         self.size = 1   # kite item story kr skte ho 
#         self.n = 0  # kite item store hai 
#         self.A=self.create_array(self.size)


#     def __len__(self):
#         return self.n
    
#     def __append__(self,item):
#         if self.n ==self.size:
#             return self.__resize(self.size*2)
#         self.A[self.n]=item
#         self.n = self.n +1 


#     def __str__(self):
#         result = ""
#         for x in range(self.n):
#             result = result +str(self.A[x]) + ','
            
#         return '['+result+']'
#     def __getitem__(self , index):
#         if 0<index<self.n:


#             return self.A[index]
#         else :
#             return 'out of range '

             
#     def __resize(self,new_capacity):
#         B=self.create_array(new_capacity)
#         self.size = new_capacity
#         for x in range(self.n):
#             B[x]= self.A[x] 
#         self.A=B

#     def create_array(self,capacity):
#         # create a c ype array statics , referential 
#         return (capacity*ctypes.py_object)()
    

# lst =Meralist()
# lst.__append__(22)
# lst.__append__(23)
# lst.__append__(7)
# lst.__append__("hello")
# lst.__append__("hello")
# lst.__append__("hiii")
# lst.__append__("ram ram sa ")
# lst.__append__("jai  shree ram ")

# # print(len(lst))
# print(lst[2])


##### pop 
import ctypes # create a datatype byusing ctypes 
class Meralist:
    def __init__(self):
        self.size = 1   # kite item story kr skte ho 
        self.n = 0  # kite item store hai 
        self.A=self.create_array(self.size)


    def __len__(self):
        return self.n
    
    def __append__(self,item):
        if self.n ==self.size:
            return self.__resize(self.size*2)
        self.A[self.n]=item
        self.n = self.n +1 


    def __str__(self):
        result = ""
        for x in range(self.n):
            result = result +str(self.A[x]) + ','
            
        return '['+result+']'
    def __getitem__(self , index):
        if 0<index<self.n:


            return self.A[index]
        else :
            return 'out of range '

             
    def __resize(self,new_capacity):
        B=self.create_array(new_capacity)
        self.size = new_capacity
        for x in range(self.n):
            B[x]= self.A[x] 
        self.A=B


    def __pop__(self):
        # return self.A[]
        if self.n ==0 :
            return """list is empty"""
        
        
        print(self.A[self.n-1] )

        self.n=self.n -1 

    def __clear__(self):
        self.n =0
        self.size =1 

    
            




    

    def __find__(self,item ):
        for x in range(self.n):
            
            if self.A[x]==item:
                
                print( x)

            else:
                return "value error "


    def __insert__(self, pos , item ):
        if self.n == self.size:
            self.__resize(self.size *2 )
        for i in range(self.n, pos,-1):
            # if i ==0:
                self.A[i] = self.A[i-1]

        self.A[pos]=item
        self.n = self.n +1 


    def __remove__(self , item):
       
        pos=self.__find__(item=item)
        if type(pos)==int:
            self.__delitem__(pos)
        else:
            return pos


    def __delitem__(self,pos ):
        for x in range(pos , self.n-1):
            self.A[x]= self.A[x+1]
            # if self.A[x]==pos
        self.n = self.n -1 
   





    def create_array(self,capacity):
        # create a c ype array statics , referential 
        return (capacity*ctypes.py_object)()
        





        
            

                

# print()
    

lst =Meralist()
# lst.__append__(22)
lst.__append__(23)
lst.__append__(24)
lst.__append__(25)
lst.__append__(26)


# lst.__append__(7)
# lst.__append__("i love you ")
# lst.__append__("i like you ")
# lst.__append__("hiii")
# lst.__append__("ram ram sa ")
# lst.__append__("jaishreeram")

# print(len(lst))
# print(lst[2])
# print(lst)
# lst.__pop__()
# lst.__pop__()
# lst.__pop__()
# lst.__clear__()
# lst.__find__(23)
# lst.index("jaishreeram")
# lst.index(678)

# print(lst)
# lst.__find__(516846)
# lst.__insert__(1,"govind")
# del[lst[2]]
# lst.__delitem__(2)
# del lst[2]
# lst.__remove__(23)
lst.__remove__(23)
print(lst)



# print("__delitem__")






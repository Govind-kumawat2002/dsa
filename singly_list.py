class Node:
    def __init__(self,item=None,next=None):
        self.item = item 
        self.next = next
# x2 = Node(5,8)
x=Node(2,4)
class Sll:
    def __init__(self , start = None):
        self.start = start
    def empty_lst(self):
        return  self.start == None
    def insert_at_start(self ,data):
        
        n = Node(item=data,next=self.start)
        self.start = n
        self.data =data

    def insert_at_last(self ,data):
        # self.start =temp
        # self.data = data
        n= Node(item=data)
        if not self.empty_lst():
            temp=self.start
            # temp = temp.next
            while temp.next is not None:
                temp = temp.next
            temp.next=n
        else:
            self.start=n

    def insert_any_position(self , position , data):
        n= Node(item=data)
        if not self.empty_lst():
            temp = self.start
            while temp.next==position:
                temp.item = n      
        return self.start==n 


    def delation_at_start(self):
        temp = self.start
        # while temp is not None:
        if not self.empty_lst():
            # temp.next=self.start.next
            # self.start.next=temp.next
            self.start=temp.next
            temp.next=None

        return self.start==None
    def delation_at_last(self,position):
        temp = self.start
        if not self.empty_lst():
            while temp.next==None:
                return temp.next==None
            

    def delation_any_position(self ,postion):
        if not self.empty_lst():
            temp =self.start
            count = 0
            while temp.next:
                count+=1
                count=postion
                temp.next= None
                temp.next=next
        return self.empty_lst()


    










            # return self.empty_lst() 
    def insert_any_position(self,position,data):
            temp = self.start
            i = 0
            while temp !=None:
                i+=1
                if i==position:
                    n = Node(item= data,next=temp.next)
                    temp.next=
                temp = temp.next

            return False  






    def search(self ,data):
            temp=self.start
            while temp !=None:
                if temp.item==data:
                    return True
                temp = temp.next

            return False 
        
            
            


my_lst=Sll()
    

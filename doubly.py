class Node:
    def __init__(self,prev=None,item = None,next=None):
        self.prev = prev
        self.item = item 
        self.next = next
# Node()
class DLL:
    def __init__(self,start =None):
        self.start = start

    def list_empty(self):
        return self.start==None
    def insert_at_start(self,data ):
        # if not self.list_empty():
            
        n= Node(prev=None,item=data,next=self.start)
        self.start=n
        self.data= data
    def insert_at_last(self ,data):
        temp = self.start
        n = Node(prev=temp.next,item=data,next=None)
        if not  self.list_empty():
            while temp.next is not None:
                temp = temp.next
            temp.next=n

        else:
            self.start=n
    def insert_any_position(self ,data, position):
        if not self.list_empty():
            count = 0
            Temp =self.start
            while count==position:
                n = Node(prev=Temp.item,item= data , next= self.start.next)
                count+=1
                return
        else:
            self.start=n










        








        # if position==0:
        #     self.insert_at_start(data)
        #     return

        # temp = self.start
        # count = 0
        # while temp is not None and count <position:

        #     Temp = temp.next
        #     count+=1
        # if temp is not None:
        #     self.insert_at_last(data)
        # else:
        #     new_node = Node(prev=self.start.prev,item=data,next=n.next)
        #     if self.start.prev is not None:
        #         self.start.next=n
        #     self.start.prev = n  
        # if not self.list_empty():
    def display(self):
        """Display the contents of the linked list """
        total_element = []
        temp = self.start
        while temp:
            total_element.append(temp.item)
            temp = temp.next
        print("->".join(map(str,total_element)))
n = Node()
# n = Node(item=455)

x=DLL()
x.insert_at_start(55)
x.insert_at_last(0000000)
x.insert_at_start(22)
x.insert_at_last(000)
x.insert_any_position(888,1)




# x.list_empty()
x.display()






        #     def display(self):
        # """ Display the contents of the linked list """
        # elements = []
        # current = self.start
        # while current:
        #     elements.append(current.data)
        #     current = current.next
        # print(" -> ".join(map(str, elements)))



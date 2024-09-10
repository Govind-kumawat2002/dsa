class Node:
    def __init__(self,item=None , next=None):
        self.item = item 
        self.next = next
n=Node()

class SLL():
    def __init__(self,start = None):
        self.start = start 
    

    # check list is empty
    def empty_lst(self):
        return self.start==None
    


    # insert a start 
    def insert_at_start(self,data):
        n = Node(item=data ,next=self.start)
        self.start=n
        self.data =data


    #insert a last 
    def insert_at_last(self ,data):
        # while list is not empty
        n = Node(item=data)
        if not self.empty_lst():
            temp = self.start
            while temp.next!=None:
                temp.item = data



        else:
            self.start = n 





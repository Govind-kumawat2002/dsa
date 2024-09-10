class Node:
    def __init__(self, value):
        self.value = value  # The value of the node
        self.next = None    # Reference to the next node
    
class LinkedList:
    def __init__(self):
        self.head = None  # The first node in the list

    def append(self, value):
        """ Add a node with the given value to the end of the list """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def prepend(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current=self.head
        self.head=new_node
        new_node.next=current
    def delation_any_value_node(self,value):
        if not self.head:            
            return
        current = self.head
        if current.value==value:
            self.head=current.next
            return        
        while current.next:
            last=current
            current=current.next            
            if current.value==value :
                last.next=current.next
                return
            
        if current.value==value:
            last.next=None
            return
                

            # current+=1
            

    def display(self):
        """ Display the contents of the linked list """
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(" -> ".join(map(str, elements)))

newList=LinkedList()
newList.append(56)
newList.append(354)
newList.prepend(354)
newList.delation_any_value_node(34)
newList.display()
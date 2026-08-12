class Node: 
    def  __init__(self, data = None):  
        self.data = data 
        self.next = None 
1class SinglyLinkedList: 
    def __init__(self):   
        self.first = None   
    def insertFirst(self, data): 
        temp = Node(data)         
        temp.next=self.first 
        self.first=temp             
    def removeFirst(self): 
        if(self.first== None): 
            print("list is empty") 
        else: 
            cur=self.first 
            self.first=self.first.next 
            print("the deleted item is",cur.data)             
    def display(self): 
        if(self.first== None): 
            print("list is empty")
            return 
        cur = self.first 
        while(cur): 
          print(cur.data, end = " ") 
          cur = cur.next      
sll = SinglyLinkedList() 
while(True): 
    ch = int(input("\nEnter your choice 1-insert 2-delete 3-display 4-exit :")) 
    if(ch == 1): 
        item = input("Enter the element to insert:") 
        sll.insertFirst(item) 
        sll.display()         
    elif(ch == 2): 
        sll.removeFirst() 
        sll.display()     
    elif(ch == 3): 
        sll.display() 
    else: 
        break 
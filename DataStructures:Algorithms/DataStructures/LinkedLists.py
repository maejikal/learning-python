class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.pointer
            
    def addStart(self, new_data):
        new_node = Node(new_data)
        new_node.pointer = self.head
        self.head = new_node
            
    def addEnd(self, new_data):
        new_node = Node(new_data)
        current = self.head
        #check if the linked list is empty
        #if linked list is empty, new_node becomes the head node
        if current == None:
            self.head = new_node
            return None
        
        else: #linked list is not empty
            while current.pointer != None:#find the last node in the linked list
                current = current.pointer
                
            current.pointer = new_node
            return None
        
    def addindex(self, index, new_data):
        #the linked list is zero index
        if index == 0:
            self.addStart(new_data)
            return None
        current = self.head
        count = 1 #start at 1 as self.head is the 1st count
        while current != None:
            if count == index:
                new_node = Node(new_data)
                new_node.pointer = current.pointer
                current.pointer = new_node
                return None
            else:
                current = current.pointer
                count += 1
            
    #searching linked lists            
    def search_iter(self, target):
        if self.head == None:
            return "empty linked list"
        
        current = self.head
        while current != None:
            if current.data == target:
                return True
            current = current.pointer
        return False
    
    def search_recur(self, target):
        def recur_helper(current, target):
            if current == None:
                return False
            elif current.data == target:
                return True
            else:
                return recur_helper(current.pointer, target)
            
        return recur_helper(self.head, target)
    
    def deleteNode(self, target):
        #delete the 1st node with target data
        if self.head == None:
            return "empty linked list"
        #if the head node contains the target
        elif self.head.data == target:
            current = self.head
            self.head = self.head.pointer
            current.data = None
        else:
            prev = None
            current = self.head
            delete_flag = 0
            while current != None:
                if current.data == target:
                    delete_flag = 1
                    break
                else:
                    prev = current
                    current = current.pointer
                    
            if delete_flag == 0:
                return "target not found"
            else:
                current.data = None
                prev.pointer = current.pointer
                return "target deleted"
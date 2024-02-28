class Node:
    def __init__(self, data):
        self.data = data
        self.left = None    # this shall point to the left child node in the BST
        self.right = None   # this shall point to the right child node in the BST

#dynamic memory BST
class BST:
    def __init__(self):
        self.root = None
        
    
    # Inserts a new node with the given data to the BST
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return None
        
        def insert_helper(cur, data):
            if data < cur.data: #compare new data with current node data
                if cur.left == None: #if left side is empty
                    cur.left = Node(data)
                else:#left side is not empty
                    insert_helper(cur.left, data) #recursive call to insert_helper on left branch
            elif data > cur.data:
                if cur.right == None:
                    cur.right = Node(data)
                else:
                    insert_helper(cur.right, data)
                    
        insert_helper(self.root, data) #since self.root != None, call insert_helper to insert
           
        
    # Searches for a node with the given data in the BST
    # Returns True when found, and False otherwise
    def search(self, data):
        if self.root == None:
            return False
        
        def search_helper(cur, target):
            if cur == None:
                return False
            elif target > cur.data:
                return search_helper(cur.right, target)
            elif target < cur.data:
                return search_helper(cur.left, target)
            elif target == cur.data:
                return True
        
        return search_helper(self.root, target)
        
    
    # Prints out the result of pre-order traversal of the BST
    def preOrder(self):
        if self.root == None:
            return "Tree is empty!!!"
        
        def pre_helper(cur):
            print(cur.data) #root
            
            if cur.left != None:#left
                pre_helper(cur.left)
                
            if cur.right != None:#right
                pre_helper(cur.right)
            return None #implied if return is absent
                
        pre_helper(self.root)
                

    # Prints out the result of in-order traversal of the BST
    def inOrder(self):
        if self.root == None:
            return "Tree is empty!"
        
        def in_helper(cur):
            if cur.left != None: #left
                in_helper(cur.left)
            
            print(cur.data) #root
            
            if cur.right != None:
                in_helper(cur.right)
                
        in_helper(self.root)
            
            
    # Prints out the result of post-order traversal of the BST
    def postOrder(self):
        if self.root == None:
            return "Tree is empty"
        
        def post_helper(cur):
            if cur.left != None:
                post_helper(cur.left)
                
            if cur.right != None:
                post_helper(cur.right)
                
            print(cur.data)
            
        post_helper(self.root)
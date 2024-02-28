#hash table class
class HashTable:
    def __init__(self, n):
        self.ht = [None] * n
        self.n = n
        
    def hash_func(self, key):
        total = 0
        for item in key:
            total += ord(item)
        return total % self.n
    
    def insert(self, data):
        i = self.hash_func(data[0]) #determine the index number to store the data in
        self.ht[i] = data #store the data at that index number
        
    def search(self, key):
        i = self.hash_func(key)
        return self.ht[i]
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.previous = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.previous = self.head
        
    def add_node(self, node):
        node.previous = self.head
        node.next = self.head.next
        
        self.head.next.previous = node
        self.head.next = node
    
    def remove_node(self,node):
        previous_node = node.previous
        next_node = node.next
        
        previous_node.next = node.next
        next_node.previous = previous_node
    
    def move_to_head(self, node):
        
        self.remove_node(node)
        self.add_node(node)
    
    def pop_tail(self):
        current = self.tail.previous
        self.remove_node(current)
        
        return current
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1
        
        self.move_to_head(node)
        return node.value    
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        node = self.cache.get(key)
        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
            
            self.cache[key] = newNode
            self.add_node(newNode)
            
            self.size += 1
            
            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
            
        else:
            node.value = value
            self.move_to_head(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
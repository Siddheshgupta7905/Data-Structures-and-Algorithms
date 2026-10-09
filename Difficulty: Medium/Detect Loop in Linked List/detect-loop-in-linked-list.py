''' Linked List Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        slow = fast =  head
        
        while fast.next and fast.next.next:
            
            slow = slow.next
            
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
            
        
        

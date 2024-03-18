# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        elif head.next == None:
            return False
        else:
            count = 0
            address = []
            while head is not None:
                if id(head) not in address:
                    address.append(id(head))
                    head = head.next
                else:
                    return True
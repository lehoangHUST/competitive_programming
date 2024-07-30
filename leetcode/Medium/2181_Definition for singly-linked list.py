# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_merge_node = new_head = ListNode()
        
        # consider merge
        value = 0
        head = head.next
        while head is not None:
            if head.val != 0:
                value += head.val
            else:
                head_merge_node.next = ListNode(value, None)
                head_merge_node = head_merge_node.next
                value = 0
            head = head.next
        
        return new_head.next
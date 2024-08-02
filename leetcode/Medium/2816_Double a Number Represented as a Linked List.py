# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list = self.reverse_list(head)
        carry = 0
        current = reversed_list
        
        while current:
            new_value = current.val * 2 + carry
            current.val = new_value % 10
            carry = 1 if new_value > 9 else 0
            if carry > 0 and current.next is None:
                current.next = ListNode(carry)
                break
            current = current.next
        
        result = self.reverse_list(reversed_list)
        return result
        
    def reverse_list(self, node: ListNode) -> ListNode:
        previous, current = None, node
        
        # Traverse the original linked list
        while current:
            # Store the next node
            next_node = current.next
            # Reverse the link
            current.next = previous
            # Move to the next nodes
            previous, current = current, next_node

        # Previous becomes the new head of the reversed list
        return previous
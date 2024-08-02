# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def gcd(a, b):
        """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
        while b:
            a, b = b, a%b
        return a
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value1 = head.val
        head_gcd = new_head = ListNode(value1, None)
        head = head.next
        while head is not None:
            value2 = head.val
            value = gcd(value1, value2)
            head_gcd.next = ListNode(value, None)
            head_gcd.next.next = ListNode(value2, None)
            head_gcd = head_gcd.next.next
            value1 = value2
            head = head.next
        return new_head
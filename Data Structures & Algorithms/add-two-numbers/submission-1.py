# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = 0
        val2 = 0
        multiplier = 1
        curr = l1
        while curr:
            val1 += curr.val*multiplier
            multiplier*=10
            curr = curr.next
    
        multiplier = 1
        curr = l2



        while curr:
            val2 += curr.val*multiplier
            multiplier = multiplier*10
            curr = curr.next

        val = val1+val2

        if val == 0:
            return ListNode(0)

        dummy = ListNode()
        curr = dummy

        while val>0:
            digits = val%10
            curr.next=ListNode(digits)
            curr = curr.next
            val = val//10

        return dummy.next
        
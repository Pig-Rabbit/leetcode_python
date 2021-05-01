# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        carry = 0
        p = l1
        q = l2
        while p != None or q != None:
            if p != None:
                x = p.val
                p = p.next
            else:
                x = 0
            if q != None:
                y = q.val
                q = q.next
            else:
                y = 0
            remain = x + y + carry
            carry = remain//10
            curr.next = ListNode(remain%10)
            curr = curr.next
            
        if carry == 1:
            curr.next = ListNode(1)
        return head.next
            

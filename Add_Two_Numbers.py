# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1 = []
        a2 = []
        while l1 != None:
            a1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            a2.append(l2.val)
            l2 = l2.next
        
        a3 = []
        if len(a1) > len(a2):
            quot = 0
            for i in range(len(a2)):
                remain = (a1[i] + a2[i] + quot)%10
                a3.append(remain)
                quot = (a1[i] + a2[i] + quot)//10
            for j in range(len(a2),len(a1)):
                remain = (a1[j] + quot)%10
                a3.append(remain)
                quot = (a1[j] + quot)//10
            if quot == 1:
                a3.append(1)
        elif len(a2) > len(a1):
            quot = 0
            for i in range(len(a1)):
                remain = (a1[i] + a2[i] + quot)%10
                a3.append(remain)
                quot = (a1[i] + a2[i] + quot)//10
            for j in range(len(a1),len(a2)):
                remain = (a2[j] + quot)%10
                a3.append(remain)
                quot = (a2[j] + quot)//10
            if quot == 1:
                a3.append(1)
        else:
            quot = 0
            for i in range(len(a1)):
                remain = (a1[i] + a2[i] + quot)%10
                a3.append(remain)
                quot = (a1[i] + a2[i] + quot)//10
            if quot == 1:
                a3.append(1)
        
        l3 = ListNode(a3.pop())
        while a3 != []:
            l3 = ListNode(a3.pop(), l3)
        
        return l3

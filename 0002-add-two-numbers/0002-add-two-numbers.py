# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumListNode = ListNode()
        sl = sumListNode
        print(sumListNode)
        carry = 0

        while l1 or l2 or carry:
            l1val = 0
            l2val= 0
            if l1:
                l1val = l1.val
            else:
                l1val = 0
            if l2:
                l2val = l2.val
            else:
                l2val =0
            
            sumVal = l1val+l2val+carry
            print("Sum Value:",sumVal)
            carry = sumVal//10
            quo = sumVal%10
            sl.next = ListNode(quo)

            if l1:
                l1 = l1.next
            else:
                l1=None
            
            if l2:
                l2 = l2.next
            else:
                l2=None
            
            sl = sl.next
        
        return sumListNode.next

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = []
        large = []
        temp = head
        while temp is not None:
            if temp.val < x:
                small.append(temp.val)
            elif temp.val >= x:
                large.append(temp.val)
                      
            temp = temp.next
        
        for i in large:
            small.append(i)

        
        newNode = ListNode(0)
        current = newNode
        for i in small:
            current.next = ListNode(i)
            current = current.next
        return newNode.next



            



            




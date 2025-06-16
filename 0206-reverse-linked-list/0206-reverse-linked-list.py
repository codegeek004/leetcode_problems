# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        def print_list(head):
            temp = head
            while temp is not None:
                print(temp.val, end=" ")
                list1.append(temp.val)
                temp = temp.next
        print_list(head)
        list1.reverse()
        print()
        i = 0
        temp = head
        while temp is not None:
            temp.val = list1[i]
            print(temp.val, 'ii')
            temp = temp.next
            i+=1
        x = print_list(head)
        return head
        


        
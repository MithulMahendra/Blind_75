# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        current=head
        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
       
        if list1!=None:
            current.next=list1
        else:
            current.next=list2
        return head.next

        
#Leetcode Problem : 21
#Simply create an dummy linkedlist and change the next pointer of it to list1 or list2 based on whichever element in it is smaller.

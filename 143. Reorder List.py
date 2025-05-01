# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #To find the length
        length = 0
        curr = head
        while curr != None:
            curr = curr.next
            length += 1
        curr = head

        #Divide the LL
        secondHead = None
        count = 0
        while count < length // 2:
                curr = curr.next
                count += 1
            
        secondHead = curr.next
        curr.next = None


        #Reverse the second head
        prev = None
        curr = secondHead

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        secondHead = prev


        #Merge
        curr1 = head
        curr2 = secondHead

        while curr2 != None:
            next1 = curr1.next
            next2 = curr2.next

            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2

        





        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        
        start = head
        if not head :
            return head
        while head :
            array.append( head.val )
            head = head.next
        

        array.sort()

        head = start
        for i in range( len( array )-1 ) :
            head.val = array[i]
            head = head.next
        head.val = array[-1]
        return start
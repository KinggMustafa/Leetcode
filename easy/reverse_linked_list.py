# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #whats passed in is the head of the existing list
        new_head = None #the head to our reversed list is set to none
        current = head #the current node is set to the head of the existing list (our new tail)

        while current:
            next_current = current.next #store the next node we visit bc we are going to point this node to our new list
            current.next = new_head #point to previous node (at first it is our NOne value)
            new_head = current #the new head of the list is the node we are at 
            current = next_current #go to next node, loop will continue if it is an actual value if not we have the prev stored 
        return new_head #return the last node we visit that is not none bc that is our new head

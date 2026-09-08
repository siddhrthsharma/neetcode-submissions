# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        if length == 1:
            return None

        if length == n:
            head = head.next
            return head

        node_to_delete = (length - n) + 1
        curr_index = 1
        prev = None
        curr = head

        while curr:
            if curr_index == node_to_delete:
                prev.next = curr.next
                del curr
                break
            prev = curr
            curr = curr.next
            curr_index += 1
        
        return head
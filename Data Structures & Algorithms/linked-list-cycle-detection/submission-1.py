# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # go through the entire list, if there is no "None" then there is a cycle 
        # keep track of the visited nodes already, and if you visit a node that has already been tracked then it is in a cycle
        curr = head
        seen = set()

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False
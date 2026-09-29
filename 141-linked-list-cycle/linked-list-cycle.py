# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr = head
        visited = set()
        visited.add(curr)

        while curr.next is not None:
            curr = curr.next
            if curr in visited:
                return True
            visited.add(curr)
        return False
        
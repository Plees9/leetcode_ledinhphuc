#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def size(head: ListNode) -> int:
    count = 0
    p = head
    while p != None:
        p = p.next
        count += 1
    return count
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = n = ListNode()
        k = size(head)
        h = head
        for i in range(k):
            if h.next != h:
                p.next = h.next
            h = h.next
        return n.next
        
        
# @lc code=end


#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def size(head: Optional[ListNode]) -> int:
        count = 0
        while head != None:
            head = head.next
            count += 1
        return count
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        k = size(p) - n
        if k > 0:
            for i in range(1,k,1):
                p = p.next
            
            if p.next.next != None:
                p.next = p.next.next
            else:
                p.next = None
        else:
            p = p.next
            return p
        
        return head       
# @lc code=end


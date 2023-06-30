#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newlist = sorted(nums1 + nums2)
        size = len(newlist)
        if size % 2 == 0:
                median = int(size / 2)
                result = (newlist[median] + newlist[median - 1]) / 2
                return float(result)
        else:
                return float(newlist[int(math.floor(size/2))])
        
# @lc code=end


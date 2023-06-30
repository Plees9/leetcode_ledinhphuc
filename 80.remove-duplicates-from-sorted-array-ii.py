#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-2,0,-1):
            if(nums[i]==nums[i-1] and nums[i]==nums[i+1]):
                nums.pop(i)
        return len(nums)     
# @lc code=end


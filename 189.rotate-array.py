#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            val = nums[-1]
            for j in range(len(nums) - 1,0,-1):
                nums[j] = nums[j-1]
            nums[0] = val
        
        
# @lc code=end


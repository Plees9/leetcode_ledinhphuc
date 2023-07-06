#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]
        for i in range(1, len(nums)):
            if max_jump < i:
                return False
            max_jump = max(max_jump, i + nums[i])
        return max_jump >= len(nums) - 1
        
# @lc code=end


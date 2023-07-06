#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_jump = nums[0]
        count = 0
        for i in range(1, len(nums)):
            if max_jump < i:
                return False
            max_jump = max(max_jump, i + nums[i])
        return max_jump >= len(nums) - 1
# @lc code=end


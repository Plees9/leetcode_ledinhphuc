#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a = sorted(list(map(lambda x: 0  if x < 0 else x,nums)))
        missing = 1
        for num in a:
            if num == missing:
                missing += 1
        return missing
        
# @lc code=end


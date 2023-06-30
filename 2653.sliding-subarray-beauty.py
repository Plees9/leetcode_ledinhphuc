#
# @lc app=leetcode id=2653 lang=python3
#
# [2653] Sliding Subarray Beauty
#

# @lc code=start
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        beauty = []
        for i in range(len(nums) - k + 1):
            a = nums[i:i+k]
            if sum(map(lambda x: 1 if x < 0 else 0, a)) < x:
                beauty.append(0)
            else:
                beauty.append(sorted(a)[x-1])
        return beauty
# @lc code=end


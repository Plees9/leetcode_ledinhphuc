#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        i = 0
        j = len(nums) - 1
        str_1 = ""
        str_2 = ""
        while str_1 != "begin" or str_2 != "end":
            if nums[i] != target:
                i += 1
            if nums[j] != target:
                j -= 1
            if nums[i] == target:
                str_1 = "begin"
            if nums[j] == target:
                str_2 = "end"
        return [i,j]        
# @lc code=end


#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        switch = False
        for i in range(0,len(nums) - 1,1):
            for j in range(i+1, len(nums), 1):
                if(nums[i] + nums[j] == target):
                    result.append(i)
                    result.append(j)
                    if len(result) == 2:
                        switch = True
            if switch == True:
                break
        return result      
# @lc code=end


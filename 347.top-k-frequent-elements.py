#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = list(set(nums))
        freq_nums = list(map(lambda x: nums.count(x), unique_nums))
        result = dict(zip(unique_nums,freq_nums))
        k_freq = sorted(freq_nums)[::-1]
        result_final = list(map(lambda x: get_key_by_value(result,x), k_freq[:k]))
        return result_final
# @lc code=end


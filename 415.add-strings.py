#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
sys.set_int_max_str_digits(25000)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))
        
# @lc code=end


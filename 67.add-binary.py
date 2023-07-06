#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        new_a = int(a,2)
        new_b = int(b,2)
        result = bin(new_a + new_b)
        return str(result[2:])
        
        
# @lc code=end


#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        newstr = s.strip().split(" ")
        a = list(filter(lambda x: x != '',newstr))[::-1]
        result = ''
        for i in a:
            result += i + " "
        return result.strip()
        
# @lc code=end


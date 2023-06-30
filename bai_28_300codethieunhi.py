#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
def stack(s:str):
    stack = []
    for i in s:
            if i == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
    return stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_1 = stack(s)
        stack_2 = stack(t)
        return stack_1 == stack_2
        
# @lc code=end


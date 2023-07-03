#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
def detectZeros(matrix: list[list[int]]) -> list[list[int]]:
    list = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                list.append([row,col])
    return list
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        list = detectZeros(matrix)
        for i in range(len(list)):
            row, col = list[i]
            matrix[row] = [0] * len(matrix[0])
            for j in range(len(matrix)):
                matrix[j][col] = 0
# @lc code=end


#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [0 for _ in range(numCourses)]
        adj = [[0] for _ in range(numCourses)]
        
        for list in prerequisites:
            adj[list[1]].append(list[0])
        
        def DFS(u: int):
            color[u] = 1
            for v in adj[u][1:]:
                if color[v] == 0:
                    if DFS(v) :
                        return True
                elif color[v] == 1:
                    return True
            color[u] = 2
            return False 
        for i in range(numCourses):
            if color[i] == 0:
                if DFS(i):
                    return False
        return True 
    
        
# @lc code=end


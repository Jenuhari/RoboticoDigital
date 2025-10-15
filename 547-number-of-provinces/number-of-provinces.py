class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)
        
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
                
        return count
        
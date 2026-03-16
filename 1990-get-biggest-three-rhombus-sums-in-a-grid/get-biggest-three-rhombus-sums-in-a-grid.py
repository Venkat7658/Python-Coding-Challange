

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        s = set()
        
        for i in range(m):
            for j in range(n):
                
                # radius = 0 (single cell rhombus)
                s.add(grid[i][j])
                
                k = 1
                while i-k >= 0 and i+k < m and j-k >= 0 and j+k < n:
                    total = 0
                    
                    # top → right
                    r, c = i-k, j
                    for t in range(k):
                        total += grid[r+t][c+t]
                    
                    # right → bottom
                    r, c = i, j+k
                    for t in range(k):
                        total += grid[r+t][c-t]
                    
                    # bottom → left
                    r, c = i+k, j
                    for t in range(k):
                        total += grid[r-t][c-t]
                    
                    # left → top
                    r, c = i, j-k
                    for t in range(k):
                        total += grid[r-t][c+t]
                    
                    s.add(total)
                    k += 1
        
        return sorted(s, reverse=True)[:3]
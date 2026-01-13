from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0.0
        min_y = float('inf')
        max_y = float('-inf')
        
        for _, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
        
        target = total_area / 2.0
        
        def area_below(h: float) -> float:
            area = 0.0
            for _, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += l * (h - y)
            return area
        
        low, high = min_y, max_y
        
        for _ in range(60):  
            mid = (low + high) / 2
            if area_below(mid) < target:
                low = mid
            else:
                high = mid
        
        return low
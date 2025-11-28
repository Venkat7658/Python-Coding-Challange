from collections import defaultdict
from collections import deque
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n <= 1:
            return 1
        
        count = 0
        adj_list = defaultdict(list)
        
        for u , v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        leaf_nodes = [node for node , neighbors in adj_list.items() if len(neighbors) == 1]

        queue = deque(leaf_nodes)   

        while queue:
            leaf_node = queue.popleft()
            parent_node = adj_list[leaf_node][0] if adj_list[leaf_node] else -1
            
            if values[leaf_node] % k == 0:
                count += 1
            else:
                values[parent_node] += values[leaf_node]
                
            if parent_node >= 0:
                adj_list[parent_node].remove(leaf_node)
            
            if parent_node >= 0 and len(adj_list[parent_node]) == 1:
                queue.append(parent_node)
            
        
        return count

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        
        def backtrack(curr):
            if len(curr) == n:
                result.append(curr)
                return
            
            for ch in ['a','b','c']:
                if not curr or curr[-1] != ch:
                    backtrack(curr + ch)
        
        backtrack("")
        
        if k > len(result):
            return ""
        
        return result[k-1]
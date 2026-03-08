class Solution:
    def runningSum(self, s: List[int]) -> List[int]:
        n=len(s)
        result=[]
        sum=0
        for i in range (n):
            sum=sum+s[i]
            result.append(sum)
        return result
    

        
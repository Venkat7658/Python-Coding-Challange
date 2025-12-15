class Solution:
    def getDescentPeriods(self, prices):
        ans = len(prices) 
        ct = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                ct += 1
            else:
                ans += ct * (ct - 1) // 2
                ct = 1

       
        ans += ct * (ct - 1) // 2
        return ans
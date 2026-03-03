class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return "0"
        l=2**n-1
        mid=l//2+1
        if k == mid:
            return "1"
        if k<mid:
            return self.findKthBit(n-1,k)
        else:
            bit = self.findKthBit(n - 1, l - k + 1)
            if bit == "0":
                return "1"
            else:
                return "0"
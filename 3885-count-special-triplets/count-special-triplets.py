class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        d={}
        res1=[0]*len(nums)
        for x  in range(len(nums)):
            if nums[x]*2 in d:
                res1[x]+=d[nums[x]*2]
            if nums[x] in d:
                d[nums[x]]+=1
            else:
                d[nums[x]]=1
        res2=[0]*len(nums)
        d2={}
        nums=nums[::-1]
        for x  in range(len(nums)):
            if nums[x]*2 in d2:
                res2[x]+=d2[nums[x]*2]
            if nums[x] in d2:
                d2[nums[x]]+=1
            else:
                d2[nums[x]]=1
        ans=0
        res2=res2[::-1]
        for x in range(len(res1)):
            ans+=res1[x]*res2[x]
        return ans%(10**9+7)
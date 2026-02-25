class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def sorting_rule(a):
            count=a.bit_count()
            return(count,a)
        result= sorted(arr,key=sorting_rule)
        return result
        
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0

        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0

            # Find leftmost adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            # Replace the pair with their sum
            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            ops += 1

        return ops
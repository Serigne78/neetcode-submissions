class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        mini = float('inf')
        l = 0
        s = 0

        for r in range(len(nums)):
           
            s += nums[r]

            
            while s >= target:
                diff = r - l + 1
                mini = min(mini, diff)
                s -= nums[l]
                l += 1

        if mini != float('inf'):
            return mini
        else:
            return 0

            
        
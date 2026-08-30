class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}
        for i, num in enumerate(nums):
            
            component = target - num
            if component in dicts:
                return [dicts[component], i]
            dicts[num] = i

        
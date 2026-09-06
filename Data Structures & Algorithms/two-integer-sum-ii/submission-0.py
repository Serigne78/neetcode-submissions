class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       dicts = {}

       for index ,num in enumerate(numbers):
            complement = target - num
            if complement in dicts:
                return [dicts[complement], index + 1]
            dicts[num] = index +1
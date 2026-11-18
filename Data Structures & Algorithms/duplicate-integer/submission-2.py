class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicts = {}
        for num in nums:
            if num not in dicts:
                dicts[num] = 1
            else:
                return True
        return False


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setList = set(nums)
        if len(nums) > len(setList):
            return True
        else:
            return False

        
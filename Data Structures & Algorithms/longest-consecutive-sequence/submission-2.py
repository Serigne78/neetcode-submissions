class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        long = 0

        for n in nums:
            if (n - 1) not in nset:
                lenght = 0
                while (n + lenght) in nset:
                    lenght +=1
                long = max(long, lenght)
        return long


        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longuest = 0 
        for n in nums:
            if (n-1) not in numSet:
                lenght = 0
                while (n+lenght) in numSet:
                    lenght+=1
                longuest = max(longuest, lenght)
        return longuest
        

        
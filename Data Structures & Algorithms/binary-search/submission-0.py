class Solution:
    def search(self, nums: List[int], target: int) -> int:
       

        debut = 0
        fin =len(nums) - 1 
        while (debut<= fin):
            millieu = (debut + fin ) // 2
            if target > nums[millieu]:
                debut = millieu  + 1
            elif target < nums[millieu]:
                fin = millieu - 1
            else:
                return millieu
        return -1

        

        
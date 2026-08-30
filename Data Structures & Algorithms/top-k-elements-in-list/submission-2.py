class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = {}
        for num in nums:
            if num in dicts:
                dicts[num] +=1
            else:
                dicts[num] = 1
        result = sorted(dicts.keys(), key=lambda x:dicts[x], reverse=True)
        return result[:k]
       
        
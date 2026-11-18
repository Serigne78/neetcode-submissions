class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts={}
        for num in nums:
            if num not in dicts:
                dicts[num] = 1
            else:
                dicts[num] += 1
        l = sorted(dicts.keys(), key=lambda x: dicts[x], reverse=True)
        return l[:k]
            
        
        
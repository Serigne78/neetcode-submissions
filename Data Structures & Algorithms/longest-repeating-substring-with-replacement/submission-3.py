class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] +=1
            else:
                count[s[i]] = 1
            while (i - l +1) - max(count.values())> k:
                count[s[l]] -=1
                l+=1
            res = max(res, i - l +1) 
        return res

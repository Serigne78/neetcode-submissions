class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts_s = {}
        dicts_t = {}

        for test_s in s:
            if test_s not in dicts_s:
                dicts_s[test_s] = 1
            else:
                dicts_s[test_s] += 1
        for test_t in t:
            if test_t not in dicts_t:
                dicts_t[test_t] = 1
            else:
                dicts_t[test_t] += 1
        return (dicts_s == dicts_t)

        
       
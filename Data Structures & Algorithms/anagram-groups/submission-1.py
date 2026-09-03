class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        for s in strs:
            a = "".join(sorted(s))
            if a not in dicts:
                dicts[a] = [s]
            else:
                dicts[a].append(s)
        return list(dicts.values())
        

            

        
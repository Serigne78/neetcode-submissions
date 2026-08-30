class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        
        for i in range(len(strs)):
            tri = "".join(sorted(strs[i]))
            dicts.setdefault(tri, []).append(strs[i])
        return list(dicts.values())
        

            

        
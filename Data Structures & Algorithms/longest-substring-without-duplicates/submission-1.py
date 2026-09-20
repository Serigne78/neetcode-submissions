class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        compt = set()  # Un set (ou une liste) pour la fenêtre actuelle
        l = 0 
        maxi = 0 
        
        for r in range(len(s)):
            # Tant qu'on a un doublon, on rétrécit la fenêtre par la gauche
            while s[r] in compt:
                compt.remove(s[l])
                l += 1
            
            # On ajoute le nouveau caractère
            compt.add(s[r])
            
            # On met à jour le maximum
            maxi = max(maxi, r - l + 1)
            
        return maxi
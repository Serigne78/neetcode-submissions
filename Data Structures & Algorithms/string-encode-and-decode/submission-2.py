class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for st in strs:
            result += str(len(st)) + "#" + st
        return result

    def decode(self, s: str) -> List[str]:
        r = []
        i = 0
        
        while i < len(s):
            # 1. Trouver le délimiteur '#'
            j = i
            while s[j] != "#":
                j += 1
            
            # 2. Récupérer la taille (gère 1 chiffre, 2 chiffres ou plus)
            length = int(s[i:j])
            
            # 3. Extraire le mot d'un coup sans boucle interne
            start = j + 1
            end = start + length
            r.append(s[start:end])
            
            # 4. Sauter directement au mot suivant
            i = end
            
        return r
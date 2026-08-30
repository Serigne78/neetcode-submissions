class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Nettoyer la chaîne
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        
        # Comparer directement avec la version inversée
        return cleaned == cleaned[::-1]
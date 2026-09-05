class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s).replace(" ","").lower()
        l = 0 
        r = len(s) -1
        while l < r:
            if s[l].isalnum() == False:
                l+=1
                continue
            if s[r].isalnum() == False:
                r-=1
                continue
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True


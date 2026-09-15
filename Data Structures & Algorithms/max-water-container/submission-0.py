class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l= 0
        r=len(heights) - 1
        maxi = 0

        while l < r: 
            largeur = abs((l+1) - (r+1))
            longueur = min(heights[l],  heights[r])
            vol = largeur * longueur 
            if vol > maxi:
                maxi = vol
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxi

        
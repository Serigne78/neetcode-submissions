class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxi = 0
        while l < r:
            aire = min(heights[l], heights[r]) * (r - l)   # 1. mesurer
            maxi = max(maxi, aire)
            if heights[l] < heights[r]:                   # 2. bouger le plus petit
                l += 1
            else:
                r -= 1
        return maxi
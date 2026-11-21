class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l = 0
        r = len(arr) - 1

        while r - l + 1 > k:
            distance_gauche = abs(arr[l] - x)
            distance_droite = abs(arr[r] - x)

            if distance_gauche > distance_droite:
                l += 1
            else:
                r -= 1
        return arr[l:r + 1]
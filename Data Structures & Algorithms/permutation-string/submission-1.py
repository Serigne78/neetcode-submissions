class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        check = []

        s1 = list(s1)
        s1_fast_memory = set(s1)

        for r in range(len(s2)):
            if s2[r] not in s1_fast_memory:
                l = r + 1
                check = []
            else:
                check.append(s2[r])

                while len(check) > len(s1):
                    check.pop(0)
                    l += 1

                if len(check) == len(s1):
                    if sorted(check) == sorted(s1):
                        return True

        return False
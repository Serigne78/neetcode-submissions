class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        reponse = [0] * len(temperatures)
        pile = []

        for i in range(len(temperatures)):
            while pile and temperatures[i] > temperatures[pile[-1]]:
                j = pile.pop()
                reponse[j] = i - j 
            pile.append(i)
        return reponse
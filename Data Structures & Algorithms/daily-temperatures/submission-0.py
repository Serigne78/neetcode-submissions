class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        reponse = [0] * len(temperatures)
        pile = []                                        # indices des jours en attente
        for i in range(len(temperatures)):
            while pile and temperatures[i] > temperatures[pile[-1]]:
                j = pile.pop()                           # le jour j a trouvé plus chaud
                reponse[j] = i - j                       # nombre de jours d'attente
            pile.append(i)                               # le jour i attend à son tour
        return reponse
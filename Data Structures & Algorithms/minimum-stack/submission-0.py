class MinStack:

    def __init__(self):
        self.liste = []
        self.mini = []

    def push(self, val: int) -> None:
        self.liste.append(val)

        # On enregistre le minimum valable à ce nouvel étage
        if not self.mini:
            self.mini.append(val)
        elif val < self.mini[-1]:
            self.mini.append(val)
        else:
            # Le minimum n'a pas changé : on répète l'ancien minimum pour garder la même hauteur
            self.mini.append(self.mini[-1])

    def pop(self) -> None:
        # Les deux piles ont la même hauteur : on dépile simplement les deux sommets en O(1)
        self.liste.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.liste[-1]

    def getMin(self) -> int:
        return self.mini[-1]
import random

class Pool():
    def __init__ (self):
        self.pool = [[],[],[],[]]

    def printpool(self):
        print(self.pool)

    def addPool(self, unit: dict):
        if unit.get('Rating') == 3:
            self.pool[0].append(unit)
        elif unit.get('Rating') == 4:
            self.pool[1].append(unit)
        elif unit.get('Rating') == 5:
            self.pool[2].append(unit)
        elif unit.get('Rating') == 6:
            self.pool[3].append(unit)

    def roll(self):
        Choices = random.choices(self.pool, weights=(40,50,8,2), k = 10)
        res = []
        for i in range(len(Choices)):
            Pulled = random.choice(Choices[i]) 
            res.append(Pulled.get('Name') + ' - ' + str(Pulled.get('Rating') ) + "★" )
        res = '\n'.join(res)
        return res
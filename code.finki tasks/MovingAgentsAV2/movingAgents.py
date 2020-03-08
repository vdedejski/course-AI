class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): # To_String method
        return f'Position ({self.x}, {self.y})'

    def move(self):
        pass

class LeftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x,y)

    def move(self):
        self.x -= 1
class RightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x += 1
class UpAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y += 1
class DownAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y -= 1


if __name__ == '__main__':
    listOfInputs = []
    for i in range(8):
        listOfInputs.append(int(input())) #Input Agent Positions

    la = LeftAgent(listOfInputs[0], listOfInputs[1])
    print(la)
    for i in range(5):
        la.move()
        print(f'Step: {i}, {la}')

    ra = RightAgent(listOfInputs[2], listOfInputs[3])
    print(ra)
    for i in range(5):
        ra.move()
        print(f'Step: {i}, {ra}')

    ua = UpAgent(listOfInputs[4], listOfInputs[5])
    print(ua)
    for i in range(5):
        ua.move()
        print(f'Step: {i}, {ua}')

    da = DownAgent(listOfInputs[6], listOfInputs[7])
    print(da)
    for i in range(5):
        da.move()
        print(f'Step: {i}, {da}')

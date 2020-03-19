from random import randint

class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, position):
        self.x = position[0]
        self.y = position[1]

        print(f'[{self.x}, {self.y}]')
        # print(f'I moved {position[2]}, coordinates: {self.x}, {self.y}')

class Game:

    def __init__(self, matrix=None):
        if matrix is None:
            matrix = []
        self.matrix = matrix

class Pacman:

    def __init__(self):
        self.player = Player()
        self.game = Game(None)
        self.isThereDots = None

    def remainingDots(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '.': return True

        return False

    def play_game(self, matrix, height, width):
        self.game = matrix
        wantedPositions = []
        normalPositions = []

        isThereDots = self.remainingDots(self.game)
        # print(self.game)

        if isThereDots == False:
            print('Nothing to do here')
        else:
            while isThereDots:
                wantedPositions = []
                normalPositions = []
                # Looking for wanted positions

                # RightSide
                if self.player.y + 1 != width:
                    if self.game[self.player.x][self.player.y + 1] == '.':
                        wantedPositions.append([self.player.x, self.player.y + 1, 'right'])
                    else:
                        normalPositions.append([self.player.x, self.player.y + 1, 'right'])

                # LeftSide
                if self.player.y > 0:
                    if self.game[self.player.x][self.player.y - 1] == '.':
                        wantedPositions.append([self.player.x, self.player.y - 1, 'left'])
                    else:
                        normalPositions.append([self.player.x, self.player.y - 1, 'left'])

                # Top Move
                if self.player.x != 0:
                    if self.game[self.player.x - 1][self.player.y] == '.':
                        wantedPositions.append([self.player.x - 1, self.player.y, 'top'])
                    else:
                        normalPositions.append([self.player.x - 1, self.player.y, 'top'])

                # Down Move
                if self.player.x + 1 != height:
                    if self.game[self.player.x + 1][self.player.y] == '.':
                        wantedPositions.append([self.player.x + 1, self.player.y, 'down'])
                    else:
                        normalPositions.append([self.player.x + 1, self.player.y, 'down'])

                # print(f'Positions avaliable: {wantedPositions}')

                if len(wantedPositions) > 0:
                    randomPosition = randint(0, len(wantedPositions) - 1)
                    self.player.move(wantedPositions[randomPosition])
                    self.game[wantedPositions[randomPosition][0]][wantedPositions[randomPosition][1]] = '#'

                else:
                    randomPosition = randint(0, len(normalPositions) - 1)
                    self.player.move(normalPositions[randomPosition])

                isThereDots = self.remainingDots(self.game)


if __name__ == '__main__':

    height = int(input())
    width = int(input())

    matrix = []

    for i in range(height):
        li = list(input())
        matrix.append(li)

    pacman = Pacman()
    pacman.play_game(matrix, height, width)

    # print(matrix)

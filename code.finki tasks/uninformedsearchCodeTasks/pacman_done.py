from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

obstacles = [(0, 6), (0, 8), (0, 9), (1, 2), (1, 3), (1, 4), (1, 9), (2, 9), (3, 6), (3, 9), (4, 1), (4, 5), (4, 6),
             (4, 7),
             (5, 1), (5, 6), (6, 0), (6, 1), (6, 2), (6, 9), (8, 1), (8, 4), (8, 7), (8, 8), (9, 4), (9, 7), (9, 8)]


class Pacman(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)


    def successor(self, state):

        successors = dict()

        pacman_x = state[0]
        pacman_y = state[1]
        directionn = state[2]

        if directionn == "istok":
            # NAPRED
            if pacman_x < 9:
                x_new = pacman_x + 1
                y_new = pacman_y
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))

                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, directionn)
                    successors["ProdolzhiPravo"] = state_new

            # NAZAD
            if pacman_x > 0:
                x_new = pacman_x - 1
                y_new = pacman_y
                direction = "zapad"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["ProdolzhiNazad"] = state_new

            # Levo

            if pacman_y < 9:
                x_new = pacman_x
                y_new = pacman_y + 1
                direction = "sever"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["SvrtiLevo"] = state_new
            # Desno

            if pacman_y > 0:
                x_new = pacman_x
                y_new = pacman_y - 1
                direction = "jug"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["SvrtiDesno"] = state_new

        if directionn == "zapad":
            # Napred
            if pacman_x > 0:
                x_new = pacman_x - 1
                y_new = pacman_y
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, directionn)
                    successors["ProdolzhiPravo"] = state_new

            # Nazad
            if pacman_x < 9:
                x_new = pacman_x + 1
                y_new = pacman_y
                direction = "istok"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["ProdolzhiNazad"] = state_new

            # Levo
            if pacman_y > 0:
                x_new = pacman_x
                y_new = pacman_y
                direction = "jug"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["SvrtiLevo"] = state_new

            # Desno
            if pacman_y < 9:
                x_new = pacman_x
                y_new = pacman_y + 1
                direction = "sever"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["SvrtiDesno"] = state_new

        if directionn == "sever":
            # Napred
            if pacman_y < 9:
                x_new = pacman_x
                y_new = pacman_y + 1
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, directionn)
                    successors["ProdolzhiPravo"] = state_new

            # Nazad
            if pacman_y > 0:
                x_new = pacman_x
                y_new = pacman_y - 1
                direction = "jug"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["ProdolzhiNazad"] = state_new

            # Levo
            if pacman_x > 0:
                x_new = pacman_x - 1
                y_new = pacman_y
                direction = "zapad"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["SvrtiLevo"] = state_new

            # Desno
            if pacman_x < 9:
                x_new = pacman_x + 1
                y_new = pacman_y
                direction = "istok"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["SvrtiDesno"] = state_new

        if directionn == "jug":

            # Napred
            if pacman_y > 0:
                x_new = pacman_x
                y_new = pacman_y - 1
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, directionn)
                    successors["ProdolzhiPravo"] = state_new

            # Nazad
            if pacman_y < 9:
                x_new = pacman_x
                y_new = pacman_y + 1
                direction = "sever"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["ProdolzhiNazad"] = state_new

            # Levo
            if pacman_x < 9:
                x_new = pacman_x + 1
                y_new = pacman_y
                direction = "istok"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["SvrtiLevo"] = state_new

            # Desno
            if pacman_x > 0:
                x_new = pacman_x - 1
                y_new = pacman_y
                direction = "zapad"
                if (x_new, y_new) in dotList:
                    dotList.remove((x_new, y_new))
                if (x_new, y_new) not in obstacles:
                    state_new = (x_new, y_new, direction)
                    successors["SvrtiDesno"] = state_new

        return successors



    def goal_test(self, state):
        if not dotList:
            return True
        else:
            return False

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    direction = input()
    brojNaTocki = int(input())
    dotList = list()
    for nmb in range(0, brojNaTocki):
        pozicija = input()
        pozicija = tuple(pozicija.split(", "))
        pozicija = tuple(map(int,pozicija))
        dotList.append(pozicija)


    pacman = Pacman((x, y, direction, dotList))

    # result = breadth_first_graph_search(pacman)
    # print(result.solution())
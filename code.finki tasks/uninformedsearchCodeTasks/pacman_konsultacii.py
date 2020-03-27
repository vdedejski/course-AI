
def SvrtiDesno(x, y, side, obstacle_list):
    if side == 'istok':
        new_side = 'jug'
        while x < 10 and [x + 1, y] not in obstacle_list:
            x += 1
        return [x, y, new_side]

    if side == 'zapad':
        new_side = 'sever'
        while x > 0 and x < 10 and [x - 1, y] not in obstacle_list:
            x -= 1
        return [x, y, new_side]

    if side == 'jug':
        new_side = 'zapad'
        while y > 0 and y < 10 and [x, y - 1] not in obstacle_list:
            y -= 1
        return [x, y, new_side]

    if side == 'sever':
        new_side = 'istok'
        while y < 10 and [x, y + 1] not in obstacle_list:
            y += 1
        return [x, y, new_side]


def SvrtiLevo(x, y, side, obstacle_list):
    if side == 'istok':  # Od istok se zavrtuvam na sever
        new_side = 'sever'
        while x > 0 and x < 10 and [x - 1, y] not in obstacle_list:
            x -= 1
        return [x, y, new_side]

    if side == 'zapad':
        new_side = 'jug'
        while x < 10 and [x + 1, y] not in obstacle_list:
            x += 1
        return [x, y, new_side]

    if side == 'jug':
        new_side = 'istok'
        while y < 10 and [x, y + 1] not in obstacle_list:
            y += 1
        return [x, y, new_side]
    if side == 'sever':
        new_side = 'zapad'
        while y > 0 and y < 10 and [x, y - 1] not in obstacle_list:
            y -= 1
        return [x, y, new_side]


def ProdolzhiPravo(x, y, side, obstacle_list):
    if side == 'istok':
        new_side = 'istok'
        while y < 10 and [x, y + 1] not in obstacle_list:
            y += 1
        return [x, y, new_side]

    if side == 'zapad':
        new_side = 'zapad'
        while y > 0 and y < 10 and [x, y - 1] not in obstacle_list:
            y -= 1
        return [x, y, new_side]

    if side == 'jug':
        new_side = 'jug'
        while x < 10 and [x + 1, y] not in obstacle_list:
            x += 1
        return [x, y, new_side]

    if side == 'sever':
        new_side = 'sever'
        while x > 0 and x < 10 and [x - 1, y] not in obstacle_list:
            x -= 1
        return [x, y, new_side]


def ProdolzhiNazad(x, y, side, obstacle_list):
    if side == 'istok':
        new_side = 'zapad'
        while y > 0 and y < 10 and [x, y - 1] not in obstacle_list:
            y -= 1
        return [x, y, new_side]

    if side == 'zapad':
        new_side = 'istok'
        while y < 10 and [x, y + 1] not in obstacle_list:
            y += 1
        return [x, y, new_side]

    if side == 'jug':
        new_side = 'sever'
        while x > 0 and x < 10 and [x - 1, y] not in obstacle_list:
            x -= 1
        return [x, y, new_side]

    if side == 'sever':
        new_side = 'jug'
        while x < 10 and [x + 1, y] not in obstacle_list:
            x += 1
        return [x, y, new_side]


class Pacman(Problem):
    def __init__(self, dots_list, obstacle_list, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacle_list = obstacle_list
        self.dots_list = dots_list

    def successor(self, state):
        successors = dict()

        x = state[0]
        y = state[1]
        side = state[2]

        remove_state = [x, y]

        if remove_state in self.dots_list:
            self.dots_list.remove(remove_state)

        x_new, y_new, side_new = ProdolzhiPravo(x, y, side, self.obstacle_list)
        if x_new != x or y_new != y:
            successors['ProdolziPravo'] = (x_new, y_new, side_new)

        x_new, y_new, side_new = ProdolzhiNazad(x, y, side, self.obstacle_list)
        if x_new != x or y_new != y:
            successors['ProdolziNazad'] = (x_new, y_new, side_new)

        x_new, y_new, side_new = SvrtiLevo(x, y, side, self.obstacle_list)
        if x_new != x or y_new != y:
            successors['SvrtiLevo'] = (x_new, y_new, side_new)

        x_new, y_new, side_new = SvrtiDesno(x, y, side, self.obstacle_list)
        if x_new != x or y_new != y:
            successors['SvrtiDesno'] = (x_new, y_new, side_new)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        if len(self.dots_list) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    player_x = int(input())
    player_y = int(input())

    look = str(input())
    dots_list = []

    n = int(input())
    for i in range(n):
        dots_list.append(input().split(','))

    obstacle_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 6],
                     [1, 0], [1, 8], [1, 9],
                     [2, 8], [2, 9], [2, 4],
                     [3, 0], [3, 3], [3, 4], [3, 5],
                     [4, 4],
                     [5, 1], [5, 8], [5, 9],
                     [6, 1],
                     [7, 1], [7, 6],
                     [8, 4], [8, 5], [8, 6], [8, 8],
                     [9, 6]]

    pacman = Pacman(dots_list, obstacle_list, (player_x, player_y, look))

    result = breadth_first_graph_search(pacman)
    print(result)

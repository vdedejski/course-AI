from constraint import *

def FirstRow(tuple1, tuple2, tuple3, tuple4):
    print(tuple1[0])
    # sum = tuple1[0] + tuple2[0] + tuple3[0] + tuple4[0]
    # print(sum)
    return 7

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    variables = [(1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 1), (2, 2), (2, 3), (2, 4),
                 (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 1), (4, 2), (4, 3), (4, 4)]

    domain = [0,1]

    problem.addVariables(variables, domain)

    problem.addConstraint(FirstRow, ((1, 1), (1, 2), (1, 3), (1, 4)))

    print(problem.getSolution())

from constraint import *

def TupleRow(tuple1, tuple2, tuple3, tuple4):
    sum = tuple1[1] + tuple2[1] + tuple3[1] + tuple4[1]
    return sum

def TupleCol(tuple1, tuple2, tuple3, tuple4):
    sum = tuple1[2] + tuple2[2] + tuple3[2] + tuple4[2]
    return sum

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    variables = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1),
                 (4, 1, 2), (5, 2, 2), (6, 3, 2), (7, 4, 2),
                 (8, 1, 3), (9, 2, 3), (10, 3, 3), (11, 4, 3),
                 (12, 1, 4), (13, 2, 4), (14, 3, 4), (15, 4, 4)]

    # variables = range(0, 16)
    domain = [1,2,3,4]

    problem.addConstraint(ExactSumConstraint(7), TupleRow((0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1)))
    problem.addConstraint(ExactSumConstraint(7), TupleRow((4, 1, 2), (5, 2, 2), (6, 3, 2), (7, 4, 2)))
    problem.addConstraint(ExactSumConstraint(4), TupleRow((8, 1, 3), (9, 2, 3), (10, 3, 3), (11, 4, 3)))
    problem.addConstraint(ExactSumConstraint(5), TupleRow((12, 1, 4), (13, 2, 4), (14, 3, 4), (15, 4, 4)))

    problem.addConstraint(ExactSumConstraint(3), TupleCol((0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1)))
    problem.addConstraint(ExactSumConstraint(4), TupleCol((4, 1, 2), (5, 2, 2), (6, 3, 2), (7, 4, 2)))
    problem.addConstraint(ExactSumConstraint(10), TupleCol((8, 1, 3), (9, 2, 3), (10, 3, 3), (11, 4, 3)))
    problem.addConstraint(ExactSumConstraint(10), TupleCol((12, 1, 4), (13, 2, 4), (14, 3, 4), (15, 4, 4)))

    print(problem.getSolution())

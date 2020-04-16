from constraint import *

if __name__ == '__main__':
    no = int(input())

    problem = Problem()

    domain = []
    for i in range(0, no):
        for j in range(0, no):
            domain.append((i,j))

    queens = range(1,no+1)

    problem.addVariables(queens, domain)

    # q1[0] = redica na top
    # q1[1] = kolona na top

    for queen1 in queens:
        for queen2 in queens:
            if queen2 < queen1:
                problem.addConstraint(lambda q1, q2: (q1[0] != q2[0]) and
                                                     (q1[1] != q2[1]) and
                                                     (abs(q1[0] - q2[0]) != abs(q1[1] - q2[1]))
                                                     ,
                                      (queen1, queen2))


    if no <= 6:
        solution = problem.getSolutions()
        print(len(solution))
    else:
        solution = problem.getSolution()
        print(solution)


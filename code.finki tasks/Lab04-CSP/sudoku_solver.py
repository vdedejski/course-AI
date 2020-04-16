import math

from constraint import *

if __name__ == '__main__':

    input = input()
    if input == 'BacktrackingSolver':
        problem = Problem(BacktrackingSolver())

    else:
        if input == 'RecursiveBacktrackingSolver':
            problem = Problem(RecursiveBacktrackingSolver())
        else:
            problem = Problem(MinConflictsSolver())

    variables = range(0, 81)  # Broj na polinja kako varijabili
    domain = range(1, 10)  # Domen na moznosti na sekoja varijabila

    for variable in variables:
        problem.addVariables([variable], domain)

    rowGroups = []
    counter = 0
    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            row.append(counter)
            counter += 1
        rowGroups.append(row)

    columnGroups = []
    counter = 0
    for i in range(0, 9):
        column = []
        counter = i
        for j in range(0, 9):
            column.append(counter)
            counter += 9
        columnGroups.append(column)

    groupsByThrees = [[0,1,2,9,10,11,18,19,20]]

    for i in range(0,8):
        secondGroup = []
        for i in groupsByThrees[i]:
            secondGroup.append(i+3)
        groupsByThrees.append(secondGroup)

    for group in [rowGroups, columnGroups, groupsByThrees]:
        for i in group:
            problem.addConstraint(AllDifferentConstraint(), i)

    # for group in groupsByThrees:
    #     problem.addConstraint(AllDifferentConstraint(), group)
    #
    # for group in rowGroups:
    #     problem.addConstraint(AllDifferentConstraint(), group)
    #
    # for group in columnGroups:
    #     problem.addConstraint(AllDifferentConstraint(), group)

    solutions = problem.getSolution()
    print(solutions)



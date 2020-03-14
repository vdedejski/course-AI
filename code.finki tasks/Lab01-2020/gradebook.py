from math import ceil

def sumPoints(points):
    li = [int(i) for i in points]
    grade =  ceil(sum(li)/10)
    if grade >= 6: return grade
    else: return 5

if __name__ == '__main__':
    dictionary = {}
    while True:
        s = input()
        if s == 'end': break
        listInformation = s.split(",")
        name = listInformation[0] + " " + listInformation[1]
        index = listInformation[2]
        course = listInformation[3]
        points = [listInformation[4], listInformation[5], listInformation[6]]
        totalPoints = sumPoints(points)
        tuple = [name, course, totalPoints]

        dictionary.setdefault(index, []).append(tuple)


    for x in dictionary.keys():
        print(f'\nStudent: {dictionary[x][0][0]}')
        for i in dictionary[x]:
            print(f'\t{i[1]}: {i[2]}')

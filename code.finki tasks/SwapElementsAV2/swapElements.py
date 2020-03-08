def switchPlaces(list):
    switchedList = [(y,x) for (x,y) in list]
    print(switchedList)

if __name__ == '__main__':
    list = []
    while True:
        line = str(input()).split(" ")
        if line[0] == "-1": break # Uslov za break na ciklusot
        tuple = (line[0], line[1])
        list.append(tuple)

    print(list)
    switchPlaces(list)
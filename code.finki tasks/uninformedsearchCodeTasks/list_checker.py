if __name__ == '__main__':
    tuple = (1, 2, 3, '|', '|')

    for i in tuple:
        isins = isinstance(i, int)
        print(isins)
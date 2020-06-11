from sklearn.preprocessing import OrdinalEncoder
import math
from sklearn.naive_bayes import CategoricalNB, GaussianNB

dataset = [["crvena", "sportski", "evropski", "1"],
           ["crvena", "sportski", "evropski", "0"],
           ["crvena", "sportski", "evropski", "1"],
           ["zolta", "sportski", "evropski", "0"],
           ["zolta", "sportski", "neevropski", "1"],
           ["zolta", "suv", "neevropski", "0"],
           ["zolta", "suv", "neevropski", "1"],
           ["zolta", "suv", "evropski", "0"],
           ["crvena", "suv", "neevropski", "0"],
           ["crvena", "sportski", "neevropski", "1"]]

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    encoder.fit(dataset)
    dataset = encoder.transform(dataset)

    train_set = dataset[0:math.ceil(0.9 * len(dataset))]
    test_set = dataset[math.ceil(0.9 * len(dataset)):]

    X = [train_set[i][:-1] for i in range(0, len(train_set))]
    Y = [train_set[i][-1] for i in range(0, len(train_set))]

    clf = CategoricalNB(alpha=2) # Alpha == 2, for Laplace smoothing parameter
    clf.fit(X,Y)

    accuracy = 0 # Model Accuracy
    for row in test_set:
        predict = clf.predict([row[:-1]])
        if predict == row[-1]:
            accuracy = accuracy + 1

    # print(accuracy/len(test_set)) # Print model accuracy

    entry1 = ["crvena", "suv" ,"evropski"]
    #entry2 = ["zolta", "evropski"]

    print(clf.predict(entry1))
from sklearn.preprocessing import OrdinalEncoder
import math
from sklearn.naive_bayes import CategoricalNB

if __name__ == '__main__':
    dataset = [["crvena", "evropski", "1"],
               ["crvena", "evropski", "0"],
               ["crvena", "evropski", "1"],
               ["zolta", "evropski", "0"],
               ["zolta", "neevropski", "1"],
               ["zolta", "neevropski", "0"],
               ["zolta", "neevropski", "1"],
               ["zolta", "evropski", "0"],
               ["crvena", "neevropski", "0"],
               ["crvena", "neevropski", "1"]]

    encoder = OrdinalEncoder()
    encoder.fit([dataset[i][:-1] for i in range(0, len(dataset))])

    train_set = dataset[0:math.ceil(0.9 * len(dataset))]
    test_set = dataset[math.ceil(0.9 * len(dataset)):]

    X = [train_set[i][:-1] for i in range(0, len(train_set))]
    X = encoder.transform(X)
    Y = [train_set[i][-1] for i in range(0, len(train_set))]

    clf = CategoricalNB(alpha=2) # Alpha == 2, for Laplace smoothing parameter
    clf.fit(X, Y)

    test_set_x = encoder.transform([test_set[i][:-1] for i in range(0, len(test_set))])

    accuracy = 0
    for i in range(0, len(test_set)):
        predict = clf.predict([test_set_x[i]])
        if predict[0] == test_set[i][-1]:
            accuracy += 1

    # print(accuracy / len(test_set))

    entry = ["zolta", "evropski"]
    entry = encoder.transform([entry])
    print(clf.predict(entry))

    print(clf.predict_proba(entry))


import numpy as np
import argparse
#import pdb
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

parser = argparse.ArgumentParser()
parser.add_argument("data_input")

args = parser.parse_args()


def parse_cat(raw, labels):
    cat = []
    for line in raw:
        for label in labels:
            if label in line:
                cat.append(labels.index(label))
                break
    return cat


def predict_error(clf, data, labels):
    pred = clf.predict(data)
    error = 0
    for i, v in enumerate(pred):
        if v != labels[i]:
            error += 1

    return error / len(labels)


def prune_data(data, remove):
    remove = np.where(data == remove)[1]
    return np.delete(data, remove, axis=1)


f = open(args.data_input, 'r')
raw = np.loadtxt(f, delimiter=',', skiprows=1, dtype='str')
raw = prune_data(raw, 'NA')

cat_raw = raw[:, 0]
data = raw[:, 1:].astype('float32')

cat = parse_cat(cat_raw, ['LUSC', 'COAD'])

X_train, X_test, y_train, y_test = train_test_split(data, cat, test_size=0.2)

clf = MLPClassifier(max_iter=10000).fit(X_train, y_train)
#clf = MLPClassifier(random_state=1).fit(X_train, y_train)

train_error = predict_error(clf, X_train, y_train)
test_error = predict_error(clf, X_test, y_test)

print(args.data_input)
print(f"Training error: {train_error}")
print(f"Test error: {test_error}")

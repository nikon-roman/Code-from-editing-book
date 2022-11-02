from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


digits = datasets.load_digits()
n_samples = len(digits.images)  # 1797
data = digits.images.reshape((n_samples, -1))

X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.3)

clf = MLPClassifier(hidden_layer_sizes=(100, 100))
clf.fit(X_train, y_train)

y_train_pred = clf.predict(X_train)
print((y_train_pred == y_train).mean())  # 1.0

y_test_pred = clf.predict(X_test)
print((y_test_pred == y_test).mean())  # 0.988

import os, sklearn.datasets as ds
print(os.path.join(os.path.dirname(ds.__file__), 'data'))

from sklearn.datasets import load_diabetes
df = load_diabetes(as_frame = True).frame
print(df.head())

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, r2_score

from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, confusion_matrix)

X, y = load_diabetes(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state = 42
)

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("평균오차 = %6.2f" % mean_absolute_error(y_test, pred))
print("설명력 = %7.4f" % r2_score(y_test, pred))

base = DummyRegressor(strategy = "mean")

base.fit(X_train, y_train)

pred = base.predict(X_test)

print("평균오차 = %6.2f" % mean_absolute_error(y_test, pred))
print("설명력 = %7.4f" % r2_score(y_test, pred))

y_train_c = (y_train > 140).astype(int)
y_test_c = (y_test > 140).astype(int)

clf = LogisticRegression(max_iter = 1000)
clf.fit(X_train, y_train_c)

pred = clf.predict(X_test)

print("정확도 = %.4f" % accuracy_score(y_test_c, pred))
print("정밀도 = %.4f" % precision_score(y_test_c, pred))
print("재현율 = %.4f" % recall_score(y_test_c, pred))
print("네칸짜리 표")
print(confusion_matrix(y_test_c, pred))

base = DummyClassifier(strategy = "most_frequent")
base.fit(X_train, y_train_c)

pred = base.predict(X_test)

print("정확도 = %.4f" % accuracy_score(y_test_c, pred))
print("정밀도 = %.4f" % precision_score(y_test_c, pred))
print("재현율 = %.4f" % recall_score(y_test_c, pred))
print("네칸짜리 표")
print(confusion_matrix(y_test_c, pred))
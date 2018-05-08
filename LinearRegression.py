from sklearn.linear_model import LinearRegression
import mglearn
from sklearn.model_selection import train_test_split
import numpy as np

X, y = mglearn.datasets.make_forge()

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)

clf = LinearRegression()
clf.fit(X_train,y_train)

# Linear regression finds the parameters $w$ and $b$ that minimize the mean squared
# error between predictions and the true regression targets $y$ on the training set

# here $w - weight is coef_ and $b - intercept is intercept_

#
# The intercept_ attribute is always a single float number, while the coef_ attribute is
# a numpy array with one entry per input feature. As we only have a single input feature
# in the wave dataset, lr.coef_ only has a single entry.
print("lr.coef_: {}".format(clf.coef_))
print("lr.intercept_: {}".format(clf.intercept_))

print("training set score: %f" % clf.score(X_train, y_train))
print("test set score: %f" % clf.score(X_test, y_test))

from sklearn.linear_model import Ridge

# Ridge(Alpha = 10)
ridge = Ridge()
ridge.fit(X_train,y_train)

print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))

# ridge is more restricted - less overfitting
# Makes the model less complex – better generalization
# Alpha parameter can be used to control for simplicity (default 1.0)
# Higher alpha  simpler model


from sklearn.linear_model import Lasso

lasso = Lasso()
lasso.fit(X_train,y_train)
# we increase the default setting of "max_iter",
# otherwise the model would warn us that we should increase max_iter.
# lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)
# low alpha more complex the model becomes


print("Training set score: {:.2f}".format(lasso.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lasso.score(X_test, y_test)))
print("Number of features used: {}".format(lasso.sum(lasso.coef_ != 0)))

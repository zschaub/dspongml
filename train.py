import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from joblib import dump


def main():
    data = pd.read_csv("pong_data.csv")
    X = data.iloc[:, :4]
    y = data.iloc[:, 5]

    print(X)
    print(y)

    print(X.head())
    print(y.head())

    print(X.shape)
    print(y.shape)

    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25, random_state=0)

    linear = LinearRegression()
    linear.fit(Xtrain, ytrain)
    print("Linear", linear.score(Xtest, ytest))

    lasso = Lasso(alpha=0.1)
    lasso.fit(Xtrain, ytrain)
    print("Lasso", lasso.score(Xtest, ytest))

    ridge = Ridge(alpha=0.5)
    ridge.fit(Xtrain, ytrain)
    print("Ridge", ridge.score(Xtest, ytest))

    dump(linear, 'mymodel.joblib')


if __name__ == "__main__":
    main()

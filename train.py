import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from joblib import dump


def main():
    data = pd.read_csv("pong_data.csv")
    X = data.iloc[:, :4]
    y = data.iloc[:, 5]

    print(X.head())
    print(y.head())

    print(X.shape)
    print(y.shape)

    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25, random_state=0)

    model = LinearRegression(fit_intercept=True)
    model.fit(Xtrain, ytrain)
    print(model.score(Xtest, ytest))

    dump(model, 'mymodel.joblib')


if __name__ == "__main__":
    main()

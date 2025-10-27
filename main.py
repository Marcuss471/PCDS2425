# main.py

import numpy as np
from sklearn.dummy import DummyClassifier
from sklearn.metrics import f1_score, make_scorer
from sklearn.model_selection import GridSearchCV
from evaluator import Evaluator
import data_loader
import sklearn.linear_model as skl_lm
import sklearn.discriminant_analysis as skl_da
import sklearn.neighbors as skl_knn
import sklearn.ensemble as skl_rf
import pre_processing
import plot

# Settings
np.random.seed(2)
train_percentage = 0.8
y_col = "increase_stock"
# all_x = ["time_probability","temp","dew","no_rain","humidity","precip","snowdepth","windspeed","cloudcover","visibility","hour_of_day","day_of_week", "month","hour_sin","hour_cos","day_sin","day_cos","month_sin","month_cos","summertime","weekday","holiday"]

x_of_interest = [
    "time_probability",
    "temp",
    "humidity",
    "dew",
    "no_rain",
    "no_snow",
    "good_visibility",
    "month",
    "day_of_week",
    "hour_of_day",
]


def main():
    [df, x_cols] = data_loader.get_data(x_of_interest)

    # Plot the data
    plot.scatter_matrix(df, data_loader.x_numerical)
    for numerical_col in data_loader.x_numerical:
        plot.numerical(df, numerical_col)
    for boolean_col in data_loader.x_boolean:
        plot.boolean(df, boolean_col)
    for boolean_col in data_loader.x_qualitative:
        plot.qualitative(df, boolean_col)

    # Split data into train and test
    training_size = int(df.shape[0] * train_percentage)
    train_select = np.random.choice(df.shape[0], size=training_size, replace=False)
    train_idx = df.index.isin(train_select)
    train, test = df.iloc[train_idx], df.iloc[~train_idx]

    # Process the data
    [train, test] = pre_processing.process(train, test)
    x_train, y_train = train[x_cols], train[y_col]
    x_test, y_test = test[x_cols], test[y_col]

    # Plot the data
    plot.scatter_matrix(df, data_loader.x_numerical)
    for numerical_col in data_loader.x_numerical:
        plot.numerical(df, numerical_col)
    for boolean_col in data_loader.x_boolean:
        plot.boolean(df, boolean_col)
    for boolean_col in data_loader.x_qualitative:
        plot.qualitative(df, boolean_col)

    # Set the parameters for f1 score to be the same for all models
    f1 = make_scorer(f1_score, average="binary", pos_label="high_bike_demand")
    print("\n=== BEST PARAMS ===")

    # dummy model
    dummy_model = DummyClassifier(strategy="most_frequent")
    evaluator_dummy = Evaluator(dummy_model, x_train, y_train, x_test, y_test)

    # logistic regression
    model_logistic = skl_lm.LogisticRegression(max_iter=10000)
    param_grid_LogReg = {
        "C" : np.linspace(0.01, 1, 20),
        "solver" : ["newton-cg", "lbfgs", "liblinear", "saga"],
        "penalty" : ["l1", "l2"]
        }

    grid_logistic = GridSearchCV(model_logistic, param_grid_LogReg, cv=10, n_jobs=1, scoring=f1)
    grid_logistic = grid_logistic.fit(x_train, y_train)

    print(f"LogReg:\t{grid_logistic.best_params_}")
    best_logistic = grid_logistic.best_estimator_

    evaluator_logistic = Evaluator(best_logistic, x_train, y_train, x_test, y_test)

    # QDA
    model_qda = skl_da.QuadraticDiscriminantAnalysis(reg_param=0.0)
    param_qda = {
        "reg_param": [
            0.0,
            0.1,
            0.2,
            0.21,
            0.22,
            0.23,
            0.24,
            0.25,
            0.3,
            0.5,
            1.0,
        ],
    }

    grid_qda = GridSearchCV(model_qda, param_qda, cv=10, n_jobs=-1, scoring=f1)
    model_grid_qda = grid_qda.fit(x_train, y_train)
    print(f"QDA:\t{grid_qda.best_params_}")
    best_qda = model_grid_qda.best_estimator_

    evaluator_qda = Evaluator(best_qda, x_train, y_train, x_test, y_test)

    # KNN
    model_knn = skl_knn.KNeighborsClassifier()

    param_grid_knn = {
        "n_neighbors": [3, 5, 7, 9, 11],
        "weights": ["uniform", "distance"],
        "metric": ["euclidean", "manhattan"],
    }

    grid_knn = GridSearchCV(model_knn, param_grid_knn, cv=10, n_jobs=-1, scoring=f1)
    model_grid_knn = grid_knn.fit(x_train, y_train)
    print(f"KNN:\t{grid_knn.best_params_}")
    best_knn = model_grid_knn.best_estimator_

    evaluator_knn = Evaluator(best_knn, x_train, y_train, x_test, y_test)

    # Random Forest
    model_rf = skl_rf.RandomForestClassifier()
    param_grid_rf = {
        "max_depth": [3, 5, 7, 10],
        "n_estimators": [100, 200, 300, 400, 500],
        "max_features": [10, 20, 30, 40],
    }

    grid_rf = GridSearchCV(model_rf, param_grid_rf, cv=10, n_jobs=-1, scoring=f1)
    model_grid_rf = grid_rf.fit(x_train, y_train)
    print(f"RF:\t{model_grid_rf.best_params_}")
    best_rf = model_grid_rf.best_estimator_

    evaluator_rf = Evaluator(best_rf, x_train, y_train, x_test, y_test)

    print("\n=== COMPARISON ===")
    print("Model\tAccuracy\tF1")
    print(
        f"Dummy:\t{evaluator_dummy.accuracy() * 100:.2f}% \t\t{evaluator_dummy.f1() * 100:.2f}%"
    )
    print(
        f"LReg: \t{evaluator_logistic.accuracy() * 100:.2f}% \t\t{evaluator_logistic.f1() * 100:.2f}%"
    )
    print(
        f"QDA:  \t{evaluator_qda.accuracy() * 100:.2f}% \t\t{evaluator_qda.f1() * 100:.2f}%"
    )
    print(
        f"KNN:  \t{evaluator_knn.accuracy() * 100:.2f}% \t\t{evaluator_knn.f1() * 100:.2f}%"
    )
    print(
        f"RF:   \t{evaluator_rf.accuracy() * 100:.2f}% \t\t{evaluator_rf.f1() * 100:.2f}%"
    )

    print("\n=== CONFUSION MATRIX ===")
    print("\nDummy:")
    print(evaluator_dummy.confusion_matrix())
    print("\nLReg:")
    print(evaluator_logistic.confusion_matrix())
    print("\nQDA:")
    print(evaluator_qda.confusion_matrix())
    print("\nKNN:")
    print(evaluator_knn.confusion_matrix())
    print("\nRF:")
    print(evaluator_rf.confusion_matrix())

main()
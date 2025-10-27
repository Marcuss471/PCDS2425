import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score


class Evaluator:

    def __init__(self, model, x_train, y_train, x_test, y_test):
        self.y_test = y_test

        # Train the model
        self.model = model
        self.model.fit(x_train, y_train)

        # Use the model to predict test data
        predict_prob = self.model.predict_proba(x_test)
        self.prediction = np.empty(len(x_test), dtype=object)
        self.prediction = np.where(predict_prob[:, 0] >= 0.5, *self.model.classes_)

    def precision(self):
        return precision_score(
            self.y_test, self.prediction, pos_label="high_bike_demand"
        )

    def recall(self):
        return recall_score(self.y_test, self.prediction, pos_label="high_bike_demand")

    def accuracy(self):
        return np.mean(self.prediction == self.y_test)

    def f1(self):
        return f1_score(
            self.y_test, self.prediction, average="binary", pos_label="high_bike_demand"
        )

    def confusion_matrix(self):
        return pd.crosstab(self.prediction, self.y_test)
import joblib
import logging
from pathlib import Path
import sys


import numpy as np
from sklearn.linear_model import LogisticRegression

# Add root to sys.path
# https://fortierq.github.io/python-import/
path_root_1 = Path(__file__).parents[1]
path_root_2 = Path(__file__).parents[2]
sys.path.append(str(path_root_1))
sys.path.append(str(path_root_2))

sys.path.append("..")


from load.load_data import IrisLoadData
from train.train_model import IrisTrainModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("iris_classifier.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream


class IrisClassifier:
    def __init__(self):
        load = IrisLoadData()
        train = IrisTrainModel()
        self.X, self.y = load.load_data()
        logger.info("Iris dataset loaded.")
        self.clf = train.train_model(self.X, self.y)
        logger.info("Iris model trained.")
        self.clf = self.export_model()
        logger.info("Iris model exported.")
        self.iris_type = {0: "setosa", 1: "versicolor", 2: "virginica"}
        logger.info("Iris types defined.")

    def classify_iris(
        self, sepal_length: int, sepal_width: int, petal_length: int, petal_width: int
    ) -> dict:
        """Receive the incoming features and predict the iris classification.

        Parameters
        ----------
        sepal_length : int
            Sepal length
        sepal_width : int
            Sepal width
        petal_length : int
            Petal length
        petal_width : int
            Petal width

        Returns
        -------
        dict
            Class and probability of the inference.
        """
        X = [sepal_length, sepal_width, petal_length, petal_width]
        self.model = self.load_model()
        logger.info("Iris model loaded.")
        prediction = self.model.predict_proba([X])
        result = {
            "class": self.iris_type[np.argmax(prediction)],
            "probability": round(max(prediction[0]), 2),
        }

        return result

    def export_model(self):
        joblib.dump(self.clf, "src/models/iris_model.pkl")
        return True

    def load_model(self):
        return joblib.load("src/models/iris_model.pkl")

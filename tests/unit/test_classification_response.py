from pathlib import Path
import sys

import pytest

# Add root to sys.path
# https://fortierq.github.io/python-import/
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.classifier.iris_classifier import IrisClassifier


def get_test_response_data() -> list:
    return [(4, 6, 5, 7, "virginica", 1.0), (1, 2, 3, 4, "virginica", 0.96)]


@pytest.mark.parametrize(
    "sepal_length, sepal_width, petal_length, petal_width, type_flower, accuracy",
    get_test_response_data(),
)
def test_response_parametrize(
    sepal_length: any,
    sepal_width: any,
    petal_length: any,
    petal_width: any,
    type_flower: any,
    accuracy: any,
) -> None:

    iris = IrisClassifier()
    assert type(
        iris.classify_iris(
            sepal_length,
            sepal_width,
            petal_length,
            petal_width,
        )["class"]
    ) == type(type_flower)

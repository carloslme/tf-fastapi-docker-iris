# Model refactor
## tf-fastapi-docker-iris

This is an example of how to refactor a machine learning model from a notebook to a production ready code. 

## Considerations
- Directory structure, where data transformations (if any), training, predictions, among other things, are separated.
- Modularization of code using Object Oriented Programming.
- Refactoring of functions to avoid duplication in actions.
- Optimization of actions to make the project faster and more efficient.
- Annotations to improve the reading of the code.
- Docstrings to document the code.
- Integration of logs (Logging) to record what happens in the project.
- Add unit and integration tests.
- Add file ***.gitignore***
- Add file ***requirements.txt*** with list of dependencies
- Add a ***README.md*** file to the project.


## Data

The Iris dataset is a simple, yet popular dataset consisting of 150 observations. Each observation captures the sepal length, sepal width, petal length, petal width of an iris (all in cm) and the corresponding iris subclass (one of *setosa, versicolor, virginica*).

![](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)

# Setup
## Clone the project
* Just open your terminal, go or create a directory, and run the following command:
```
$ git clone https://github.com/carloslme/tf-fastapi-docker-iris.git
```
* Change the branch
```
$ git checkout refactor
```
## Create virtual environment
* Create a virtual environment with:
```
python3 -m venv venv
```

* Activate the virtual environment

```
source venv/bin/activate
```

## Install the other libraries
Run the following command to install the other libraries.

```
pip install -r requirements.txt
```

# Usage
## Predict dummy value
* Run the following command
```
python src/classifier/predict_iris.py   
```
* You should get something like this
```
DEBUG: 2022-11-16 22:37:12,164|__main__|input_data: [3, 4, 5, 8]
INFO: 2022-11-16 22:37:12,165|iris_classifier|Iris dataset loaded.
INFO: 2022-11-16 22:37:12,199|iris_classifier|Iris model trained.
INFO: 2022-11-16 22:37:12,201|iris_classifier|Iris model exported.
INFO: 2022-11-16 22:37:12,201|iris_classifier|Iris types defined.
INFO: 2022-11-16 22:37:12,202|iris_classifier|Iris model loaded.
DEBUG: 2022-11-16 22:37:12,202|__main__|prediction: {'class': 'virginica', 'probability': 1.0}
```


## Run unit tests
* Open the terminal, and run
```
pytest tests/unit/test_classification_response.py -v
```
You should see something like this:
```
(venv) carlos.lm@192 tf-fastapi-docker-iris % pytest tests/unit/test_classification_response.py -v     
===================================================================================== test session starts =====================================================================================
platform darwin -- Python 3.7.9, pytest-7.2.0, pluggy-1.0.0 -- /Users/carlos.lm/Documents/tf-fastapi-docker-iris/venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/carlos.lm/Documents/tf-fastapi-docker-iris
collected 2 items                                                                                                                                                                             

tests/unit/test_classification_response.py::test_response_parametrize[4-6-5-7-virginica-1.0] PASSED                                                                                     [ 50%]
tests/unit/test_classification_response.py::test_response_parametrize[1-2-3-4-virginica-0.96] PASSED                                                                                    [100%]

====================================================================================== 2 passed in 1.45s ======================================================================================
```

## Build Docker image
* Run next command to build de docker image with the app.
```
docker run -d --name app -p 3000:3000 myimage
```
* Then, run this comand to run the image in a container.
```
docker run -d --name app -p 3000:3000 myimage
```
## Test request
The input is a JSON with the following fields:

* sepal_l
* sepal_w
* petal_l
* petal_w

Corresponding values are the measurements in cm.

Example request:

```
curl 'http://localhost:8080/iris/classify_iris' -X POST -H 'Content-Type: application/json' -d '{"sepal_l": 5, "sepal_w": 2, "petal_l": 3, "petal_w": 4}'
```
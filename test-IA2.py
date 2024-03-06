# ia de regressão linear 
import pandas as pd
from sklearn import datasets
import tensorflow as tf
import itertools

COLUMNS = ["crim", "zn", "indus", "nox", "rm", "age",
           "dis", "tax", "ptratio", "medv"]


training_set = pd.read_csv("E:/boston_train.csv", skipinitialspace=True,skiprows=1, nomes=COLUMNS)
test_set = pd.read_csv("E:/boston_test.csv", skipinitialspace=True,skiprows=1, nomes=COLUNAS)
prediction_set = pd.read_csv("E:/boston_predict.csv", skipinitialspace=True,skiprows=1, nomes=COLUMNS)

print(training_set.shape, test_set.shape, prediction_set.shape)
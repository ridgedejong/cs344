import numpy as np
# import tensorflow as tf
from keras.datasets import boston_housing
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

def print_structures():
    print(x_train, y_train)
    print(x_test, y_test)


print_structures()
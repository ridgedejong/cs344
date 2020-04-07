import keras
keras.__version__
import pandas as pd
pd.__version__
from keras.datasets import boston_housing
(train_data, train_targets), (test_data, test_targets) =  boston_housing.load_data()

print(
    f'training data \
        \n\tcount: {len(train_targets)} \
        \n\tshape: {train_data.shape} \
        \n\ttype: {train_targets.dtype}\n',
    f'testing data \
        \n\tcount: {len(test_targets)} \
        \n\tshape: {test_data.shape}\
        \n\ttype: {test_targets.dtype}\n',
)

testing = pd.DataFrame(test_data).copy()
training1 = pd.DataFrame(train_data).copy()
validation = training1.tail(102).copy()
training2 = training1.head(302).copy()


testing["area of crime"] = testing[7] / testing[0]
training2["area of crime"] = training2[7] / training2[0]
validation["area of crime"] = validation[7] / validation[0]
print(validation.head())
print(training2.tail())
print(testing.head())

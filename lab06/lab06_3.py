
from keras.datasets import boston_housing
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

def print_structures():
    print(
        'training examples \
                    \n\tcount: {} \
                    \n\tdimensions: {} \
                    \n\tshape: {} \
                    \n\tdata type: {}\n\n'.format(
            len(x_train),
            x_train.ndim,
            x_train.shape,
            x_train.dtype
        ),
        'testing examples \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {} \n'.format(
            len(x_test),
            x_test.ndim,
            x_test.shape,
            x_test.dtype,
        )
    )


print_structures()
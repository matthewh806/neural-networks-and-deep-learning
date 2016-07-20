import numpy as np

def init_toy_data(num_inputs=5, input_size=4, num_classes=3):
    X = 10 * np.random.rand(num_inputs, input_size)
    y = np.random.randint(0, num_classes, size=num_inputs)

    training_inputs = [np.reshape(x, (input_size , 1)) for x in X]
    training_results = [vectorized_result(j, num_classes) for j in y]
    return zip(training_inputs, training_results) 

def vectorized_result(j, num_classes):
    e = np.zeros((num_classes, 1))
    e[j] = 1.0
    return e

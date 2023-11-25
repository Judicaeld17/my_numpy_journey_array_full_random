#TASK : Create a function which take dimension of an array parameter and returns a Numpy Array fill with random integer
import numpy as np
def my_numpy_journey_array_full_random(dim1,dim2):
    return np.random.randint(0,100,size=(dim1,dim2))
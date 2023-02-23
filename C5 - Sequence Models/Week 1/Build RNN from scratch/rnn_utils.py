import numpy as np

def softmax(x):
    ex = np.exp(x-np.max(x))
    return ex/ex.sum(axis=0)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def initialize_adam(parameters):
     
     """
    Initializes v and s as two python dictionaries with:
                - keys: "dW1", "db1", ..., "dWL", "dbL" 
                - values: numpy arrays of zeros of the same shape as the corresponding gradients/parameters.
    
    Arguments:
    parameters -- python dictionary containing your parameters.
                    parameters["W" + str(l)] = Wl
                    parameters["b" + str(l)] = bl
    
    Returns: 
    v -- python dictionary that will contain the exponentially weighted average of the gradient.
                    v["dW" + str(l)] = ...
                    v["db" + str(l)] = ...
    s -- python dictionary that will contain the exponentially weighted average of the squared gradient.
                    s["dW" + str(l)] = ...
                    s["db" + str(l)] = ...
    """
     L = len(parameters)
     v={}
     s={}

     for i in range(L):
        v["dW" + str(i+1)] = np.zeros(parameters["W" + str(i+1)].shape)
        v["db" + str(i+1)] = np.zeros(parameters["b" + str(i+1)].shape)
        s["dW" + str(i+1)] = np.zeros(parameters["W" + str(i+1)].shape)
        s["db" + str(i+1)] = np.zeros(parameters["b" + str(i+1)].shape)
     

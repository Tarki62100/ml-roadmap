import numpy as np
def mean(x):
    total= 0
    for i in x:
        total+= i
    return total/len(x)

arr = np.random.random(10000000)
%timeit mean(arr)

%timeit np.mean(arr)
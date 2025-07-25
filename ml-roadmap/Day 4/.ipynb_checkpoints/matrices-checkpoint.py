from os import popen
import numpy as np
def matrix_mult(A,B):
    C = np.zeros((A.shape[0],B.shape[1]),int)
    for m in range(A.shape[0]):
        for pop in range(A.shape[1]):
            for i in range(B.shape[1]):
                print(A[m][pop] * B[pop][i])
                C[m,i] += A[m][pop] * B[pop][i]
    return C
                
A = np.array([[1,2],[3,4],[5,6]])
B = np.array([[5,7,9],[6,8,10]])
print(matrix_mult(A,B))
print(np.matmul(A,B))

            



        


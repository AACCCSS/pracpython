import numpy as np

a = np.array([[1,3],
              [2,4]])
b = np.array([[9,7],
              [6,8]])

A = np.array([[5,4,9],[7,4,1],[4,3,12]])
B = np.array([[5,6,6],[7,8,3],[9,10,12]])

c = A+B

print("Matriz A:\n ",A)
print("\nMatriz B:\n ",B)


print("\nsuma: \n",c)
    
print("\nMultiplicación de Ax2 : \n",A*2)
print("\nMultiplicación de Bx4 : \n",A*4)


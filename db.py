#https://www.pjreddie.com/media/files/mnist_train.csv
#https://www.pjreddie.com/media/files/mnist_test.csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

v = [1, 2, 3, 4, 5]
type(v)

numpy_array = np.array(v)
print(numpy_array)
print(type(numpy_array))

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(type(matrix))
print(matrix)

mnist_train= pd.read_csv("mnist_train.csv", header=None)

column_names = ["label"]

for i in range(784):
    column_names.append("px_{}".format(i + 1))
mnist_train.columns = column_names

mnist_train

matrix = mnist_train.values
print(matrix)

image = matrix[0, 1:]
image.shape

modified_image = image.reshape(28, 28)
modified_image.shape

plt.imshow(modified_image, cmap = "Greys")

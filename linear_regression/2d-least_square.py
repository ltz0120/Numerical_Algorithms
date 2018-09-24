import numpy as np
from matplotlib import pyplot as plt

# Suppose y = k*x + m
def function(k,m,x):
    return k*x+m

def least_square(x,y):
    m = np.array([1 for i in range(len(x))])
    plt.scatter(x, y)
    x = np.array(x)
    A = np.vstack((x, m)).T
    AT = A.T
    ATA = np.dot(AT, A)
    print(ATA)
    y = np.array(y)
    y = np.reshape(y, (-1, 1))
    beta = np.dot(np.dot(np.linalg.inv(ATA), AT), y)
    print(beta)
    print(y)
    output_list = []
    for i in range(len(x)):
        output_list.append(function(beta[0], beta[1], x[i]))
    return output_list



if __name__ == "__main__":
    x = [1, 2, 3, 5, 6, 7, 8, 9]
    y = [2, 4, 4, 6, 7, 8, 9, 10]
    output = least_square(x,y)
    plt.plot(x, output)
    plt.show()




# tinh binh phuong toi thieu
# cong thuc: B = (X'*X)^-1 * X'*Y
import numpy as np

def caculate_regression(data, index):
    X = []
    Y = []
    for i in range(len(data)):
        row = [1]
        for j in range(len(index)):
            row.append(data[i][index[j]])
        X.append(row)
        Y.append(data[i][6])

    X = np.array(X)
    Y = np.array(Y)


    result = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.transpose(X)), Y)
    return result
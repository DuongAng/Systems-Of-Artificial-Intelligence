import numpy as np
def check(model, data_test, columns):
    y_real = [row[6] for row in data_test]
    
    y_real_mean = sum(y_real) / len(y_real)
   
    sum_real = 0
    for i in range(len(y_real)):
        sum_real += (y_real[i] - y_real_mean) ** 2
    

    sum_predict = 0
    for i in range(len(y_real)):
        y_predict  = model[0]
        for j in range(len(columns)):
            y_predict += model[j+1] * data_test[i][columns[j]]

        sum_predict += (y_real[i] - y_predict) ** 2

    return 1 - sum_predict / sum_real
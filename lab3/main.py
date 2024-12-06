import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from dataProcessing import Data
from caculator import caculate_regression
from check import check

data = Data('Student_Performance.csv')

# Ve do thi ra
Data.draw_diagram(data.hours_studied, 'Hours studied', 10, 1)
Data.draw_diagram(data.previous_scores, 'Previous scores', 110, 10)
Data.draw_diagram(data.sleep_hours, 'Sleep hours', 11, 1)
Data.draw_diagram(data.same_question, 'Sample question papers practiced', 11, 1)
Data.draw_diagram(data.study_efficiency, 'Study efficiency', 110, 10)
Data.draw_diagram(data.performance_index, 'Performance Index', 110, 10)

# Ma hoa gia tri cua cot extracurricular_activities
data.data_encryption()
# Tinh toan cac gia tri mean va std
data.normalize_caculate()

x, y = data.set_data()

# Chia data ra thanh train and test
x_train, y_train, x_test, y_test = Data.split_data(x, y, test_size = 0.2)

data_train = []
data_test = []

for i in range(len(x_train)):
    row = []
    row.extend(x_train[i])
    row.append(y_train[i])
    data_train.append(row)

for i in range(len(x_test)):
    row = []
    row.extend(x_test[i])
    row.append(y_test[i])
    data_test.append(row)

model1 = caculate_regression(data_train, [0, 1, 2, 3, 4, 5])
result1 = check(model1, data_test, [0, 1, 2, 3, 4, 5])

model2 = caculate_regression(data_train, [1, 4])
result2 = check(model2, data_test, [1, 4])

model3 = caculate_regression(data_train, [0, 2, 4])
result3 = check(model3, data_test, [0, 2, 4])

labels = ['Model 1', 'Model 2', 'Model 3']
values = [result1, result2, result3]

print("---------------------------------------------------------------")
print(values)

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color = ['green', 'yellow', 'blue'])
plt.title('Models')
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 1.05, 0.05))
plt.tight_layout()
plt.show()

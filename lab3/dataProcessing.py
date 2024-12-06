import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import random

class Data:
    def __init__(self, data_path):
        # Doc du lieu file CSV
        data = pd.read_csv(data_path)
        # chuyển thành values cho dễ xử lý nhiều dữ liệu
        values = data.values

        #Tiền xử lý dữ liệu tìm missing, chuẩn hóa và mã hóa
        ## Tìm missing dữ liệu trước
        self.hours_studied = list(map(lambda row: self.replace_nan(row[0]), values))
        self.previous_scores = list(map(lambda row: self.replace_nan(row[1]), values))
        self.extracurricular_activities = list(map(lambda row: self.replace_empty(row[2]), values))
        self.sleep_hours = list(map(lambda row: self.replace_nan(row[3]), values))
        self.same_question = list(map(lambda row: self.replace_nan(row[4]), values))
        self.study_efficiency = list(map(lambda row: self.replace_nan(row[1]) / self.replace_nan(row[0]), values)) # giá trị mới tổng hợp từ dữ liệu cũ 
        self.performance_index = list(map(lambda row: self.replace_nan_float(row[5]), values))

        # tạo ra các giá trị mean và std (gtri trung bình và độ lệch chuẩn)
        self.mean_hours_studied = None
        self.std_hours_studied = None
        self.mean_previous_scores = None
        self.std_previous_scores = None
        self.mean_sleep_hours = None
        self.std_sleep_hours = None
        self.mean_same_question = None
        self.std_same_question = None
        self.mean_study_efficiency = None
        self.std_study_efficiency = None
        self.mean_performance_index = None
        self.std_performance_index = None

    # Mã hóa dữ liệu của extracurricular_activities từ yes no thành 0, 1
    def data_encryption(self):
        self.extracurricular_activities = list(map(lambda value : 1 if value == "Yes" else 0, self.extracurricular_activities))

    def normalize_caculate(self):
        self.mean_hours_studied = np.mean(self.hours_studied)
        self.std_hours_studied = np.std(self.hours_studied)
        self.mean_previous_scores = np.mean(self.previous_scores)
        self.std_previous_scores = np.std(self.previous_scores)
        self.mean_sleep_hours = np.mean(self.sleep_hours)
        self.std_sleep_hours = np.std(self.sleep_hours)
        self.mean_same_question = np.mean(self.same_question)
        self.std_same_question = np.std(self.same_question)
        self.mean_sleep_hours = np.mean(self.sleep_hours)
        self.std_sleep_hours = np.std(self.sleep_hours)
        self.mean_performance_index = np.mean(self.performance_index)
        self.std_performance_index = np.std(self.performance_index)
        # giá trị mới 
        self.mean_study_efficiency = np.mean(self.study_efficiency)
        self.std_study_efficiency = np.std(self.study_efficiency)

        self.normalization()
    # Chuẩn hóa dữ liệu theo công thức chuẩn hóa Z-Score 
    def normalization(self):
        self.hours_studied = list(map(lambda hours : (hours - self.mean_hours_studied) / self.std_hours_studied, self.hours_studied))
        self.previous_scores = list(map(lambda previous_scores : (previous_scores - self.mean_previous_scores) / self.std_previous_scores, self.previous_scores))
        self.sleep_hours = list(map(lambda sleep_hours : (sleep_hours - self.mean_sleep_hours) / self.std_sleep_hours, self.sleep_hours))
        self.same_question = list(map(lambda same_question : (same_question - self.mean_same_question) / self.std_same_question, self.same_question))
        self.study_efficiency = list(map(lambda study_efficiency : (study_efficiency - self.mean_study_efficiency) / self.std_study_efficiency, self.study_efficiency))
        self.performance_index = list(map(lambda performance_index : (performance_index - self.mean_performance_index) / self.std_performance_index, self.performance_index))

    # Xây dựng dữ liệu để tính công thức hồi quy tuyến tính
    def set_data(self):
        x = []
        y = []
        for i in range(len(self.hours_studied)):
            x.append([self.hours_studied[i], self.previous_scores[i], self.extracurricular_activities[i], self.sleep_hours[i], self.same_question[i], self.study_efficiency[i]])
            y.append(self.performance_index[i])

        return x, y
    
    # Chia data thành train và test data 
    @staticmethod
    def split_data(x, y, test_size):
        indices = list(range(len(x)))
        random.shuffle(indices)

        test_size = int(len(x) * test_size)
        test_indices = indices[:test_size]
        train_indices = indices[test_size:]
        x_train = [x[i] for i in train_indices]
        y_train = [y[i] for i in train_indices]
        x_test = [x[i] for i in test_indices]
        y_test = [y[i] for i in test_indices]
        return x_train, y_train, x_test, y_test

    # Ve do thi
    @staticmethod
    def draw_diagram(values, name, x, y):
        values = np.array(values)
        min_value = np.min(values)
        max_value = np.max(values)
        mean_value = np.mean(values)
        std_value = np.std(values)
        quali_25 = np.percentile(values, 25)
        quali_50 = np.percentile(values, 50)
        quali_75 = np.percentile(values, 75)

        plt.figure(figsize=(8, 5))
        plt.bar(['Min', 'Max', 'Mean', 'Std', '25%', '50%', '75%'], [min_value, max_value, mean_value
                                                                     , std_value, quali_25, quali_50, 
                                                                     quali_75], color = ['blue', 'green',
                                                                                          'orange', 'red', 'yellow', 'pink', 'black'])
        plt.title(name)
        plt.xticks(rotation = 45)
        plt.yticks(np.arange(0, x, y))
        plt.tight_layout() # chinh de khong bi trong len nhau giup dep hon
        plt.show()
    

    @staticmethod
    def replace_nan(value):
        return int(value) if not math.isnan(value) else 0
    @staticmethod
    def replace_empty(value):
        return value if value else 'No'
    @staticmethod
    def replace_nan_float(value):
        return float(value) if not math.isnan(value) else 0


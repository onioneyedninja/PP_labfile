import pandas as pd

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# data series using panda
# series is one-d array like structure which can be visualised like an Excel column
Data_series = pd.Series(data)
print("Elements in Data Series are \n", Data_series)  # printing Series created with pandas
print(type(Data_series))  # printing the datatype of element entered in series

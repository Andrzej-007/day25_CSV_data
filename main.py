
# data = []
# with open("./weather_data.csv") as file_to_open:
#     contents = file_to_open.readlines()
#
#     for content in contents:
#         strip_content = content.strip()
#         data.append(strip_content)

# import csv
#
# with open("./weather_data.csv") as file_to_open:
#     data_content = csv.reader(file_to_open)
#     temperaturs = []
#     for row in data_content:
#         if row[1] != 'temp':
#             temperaturs.append(int(row[1]))
#
# print(temperaturs)

import pandas as pd

data = pd.read_csv("./weather_data.csv")
# print(type(data))
# print('\n')
# print(data)
# print(data['temp'])  # there is the same structure as below
# print(data.temp)    # there is the same structure as above
#
# dataDict = data.to_dict()  # transfert to dictionaty
# print(dataDict)
#
# list_temp = data['temp'].to_list()
# print('\n',list_temp )
#
# average  = sum(list_temp)/len(list_temp)
# print(round(average, 2))
#
# # Series
#
# print(data['temp'].mean())
# print(data['temp'].max())

# Get Data in Raw
temp_max = data.temp.max()
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

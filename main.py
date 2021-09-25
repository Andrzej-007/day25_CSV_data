
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
# # Series -> colums
#
# print(data['temp'].mean())
# print(data['temp'].max())

# Get Data form  Raw
temp_max = data.temp.max()
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

# specific -> row starting from maonday
monday_day = data[data.day == "Monday"]
                        # below there is difference
fahreinheit_1 = (int(monday_day['temp']) * 9/5) + 32
print(f'fahreinheit_1 {fahreinheit_1}')
# another way of calculation :
                        # below there is difference
fahreinheit_2 = (int(monday_day.temp) * 9/5) + 32
print(f'fahreinheit_2 {fahreinheit_2}')


# Creating dataFrame from scratch

data_dict = {
    'students':['anna', 'greg', 'donse'],
    'scores': [4, 3, 5]
}

panda_data = pd.DataFrame(data_dict)
print(panda_data)
panda_data.to_csv("new_file_csv")

#converting into csv file 
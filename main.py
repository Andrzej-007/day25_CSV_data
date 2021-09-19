
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

import pandas

data = pandas.read_csv("./weather_data.csv")
print(data)
import pandas as pd

squirrel_data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Primary Fur Color
# list_temp = data['temp'].to_list()


squrrel_dic_temp = {}
list_temp = squirrel_data['Primary Fur Color'].to_list()
# print(f'list_temp \n{list_temp}')

for sgirel in list_temp:
    result = isinstance(sgirel , str)
    if isinstance(sgirel , str):   # <--- without data 'nan'
        if sgirel in squrrel_dic_temp:
            squrrel_dic_temp[sgirel] += 1
        else:
            squrrel_dic_temp[sgirel] = 1

''' below different option with data 'nan' '''
    # if sgirel in squrrel_dic:
    #     squrrel_dic[sgirel] += 1
    # else:
    #     squrrel_dic[sgirel] = 1

print(squrrel_dic_temp)
key_list = []
value_list = []

for k, v in squrrel_dic_temp.items():
    key_list.append(k)
    value_list.append(v)

print(key_list ,value_list )

squirrel_dic_main = {
    'colour' : key_list,
    'count': value_list
}

data_print = pd.DataFrame(squirrel_dic_main)
print(data_print)
data_print.to_csv('squirrel-count.csv')












# # with open('weather_data.csv') as csv_file:
# #     list_weather_data = csv_file.readlines()
# # print(list_weather_data)
#
# # import csv
# #
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temp = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temp.append(int(row[1]))
# # print(temp)
#
# #🐼🐼🐼🐼 Pandas
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
#
# #Data Frames
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # #Series
# # data_list_temp = data['temp'].to_list()
# # print(data_list_temp)
# #
# # #average temp
# # ave_temp = round(sum(data_list_temp) / len(data_list_temp))
# # print(ave_temp)
#
# #the largest value in temp list
# # print(data['temp'].argmax()) ..... returns the index value of the largest value in series
# #print(data['temp'].max()) ..... return the largest value in the series
#
# #print the row with the highest tempratures
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday)
# #now convert monday's temp to farenheit
# monday_temp_celsius = monday.temp
# monday_temp_farenheit = (monday_temp_celsius * 9/5) + 32
# print(monday_temp_farenheit)

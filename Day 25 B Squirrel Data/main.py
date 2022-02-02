import pandas

data_frame = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# create a new data frame containing only the color of squirrels and how many there are

black_squirrels = data_frame[data_frame['Primary Fur Color'] == 'Black']
grey_squirrels = data_frame[data_frame['Primary Fur Color'] == 'Gray']
cinnamon_squirrel = data_frame[data_frame['Primary Fur Color'] == 'Cinnamon']

total_black_squirrels = len(black_squirrels)
total_grey_squirrels = len(grey_squirrels)
total_cinnamon_squirrels = len(cinnamon_squirrel)

squirrel_count = {
    'Fur Color': ["Black", "Gray", "Cinnamon"],
     "Count": [total_black_squirrels, total_grey_squirrels, total_cinnamon_squirrels]
}
print(squirrel_count)

# create the dataframe
data_frame = pandas.DataFrame(squirrel_count)
#
# create csv file of squirrel count
data_frame.to_csv('squirrel_count.csv')

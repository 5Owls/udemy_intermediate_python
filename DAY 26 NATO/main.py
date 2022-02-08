import pandas

# create dataframe
df_nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary, not using to_dict because it gives a funny output
# using dict comprehension
dict_nato = {row.letter: row.code for (index, row) in df_nato.iterrows()}

# get user input
user_input = input("What word do you want to NATO? ").upper()

# create an output list where each letter in input has the corresponding code in dict_nato/ LONG WAY/... first try
# output_nato = []
# for letter in user_input:
#     for key in dict_nato:
#         if letter == key:
#             output_nato.append(dict_nato[key])
# print(output_nato)

#comprehension style/dr angela style
output = [dict_nato[letter] for letter in user_input]
print(output)

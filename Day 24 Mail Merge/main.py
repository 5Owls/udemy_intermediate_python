'''At first I tried using lists but that got complicated quickly, at least for me, then I used strings and done. '''
str_template = ''
for sentence in open('./Input/Letters/starting_letter.txt'):
    str_template = str_template + sentence
# print(str_template)

for name in open('./Input/Names/invited_names.txt', 'r'):
    str_name = name.strip()
    new_template_letter = str_template.replace('[name]', str_name)
    with open(f'./Output/ReadyToSend/{name}.txt', 'w') as file:
        file.write(new_template_letter)

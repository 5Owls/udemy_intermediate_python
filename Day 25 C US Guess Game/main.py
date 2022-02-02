import time
import turtle
import pandas

screen = turtle.Screen()
screen.title(f"U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# dataframe
data_frame = pandas.read_csv("50_states.csv")

score = 0
# make a list of the states colomn
list_of_states = data_frame['state'].to_list()
list_of_x_cor = data_frame['x'].to_list()
list_of_y_cor = data_frame['y'].to_list()

list_of_guessed_answers = []
list_of_states_not_guessed = []

for i in range(0, 5):
    # input from user
    answer_state = screen.textinput(title=f"Guess the state {score}/50", prompt="Type in a state name: ").title()

    # is the answer in the list of states
    if answer_state in list_of_states:
        list_of_guessed_answers.append(answer_state)
        score += 1
        # get the coordinates
        index_of_state = list_of_states.index(answer_state)
        x_cor = list_of_x_cor[index_of_state]
        y_cor = list_of_y_cor[index_of_state]

        # create a turtle so we can name the state
        state_name_turtle = turtle.Turtle()
        state_name_turtle.penup()
        state_name_turtle.hideturtle()
        state_name_turtle.goto(x_cor, y_cor)
        state_name_turtle.write(arg=answer_state, font=("Arial", 10, 'normal'), align='center')
    else: #my little extra twist
        wrong_turtle = turtle.Turtle()
        wrong_turtle.penup()
        wrong_turtle.hideturtle()
        wrong_turtle.color('red')
        wrong_turtle.write(arg="WRONG!", font=("Arial", 15, 'normal'), align='center')
        time.sleep(0.3)
        wrong_turtle.clear()
        
# save the list to a csv
for state in list_of_states:
    if state not in list_of_guessed_answers:
        list_of_states_not_guessed.append(state)

# create a dataframe
learn_data = pandas.DataFrame(list_of_states_not_guessed)
#create csv
learn_data.to_csv("names_not_remembered.csv")

print(learn_data)
turtle.mainloop()  # alternative for exitonclick event

## ALTERNATIVE
"""🛠🛠🛠🛠🛠🛠
Using values in a row directly instead of making everything lists:
list of states = data_frame.to_list()
if answer in list of states:
row of the state variable = data_frame[data_frame.state == answer]
state name turtle.goto(int(row_of_state_variable.x), int(row_of_state_variable.y))


instead of using a for loop
create a list of correct guesses and loop until the list is fille dup with 50 states.
in other words: This game will keep on going until you have guessed all fifty states. It wont stop until you are a states master...
unless i use a keyword like exit to end the game.


# 🦄🦄🦄 The following code is to get the coordinates of
# where i click on my screen.
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
"""

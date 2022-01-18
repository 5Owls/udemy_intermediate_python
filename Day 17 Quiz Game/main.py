# display question from data file
from data import question_data
from os import system


def clear():
    system('clear')


score = 0
for i in range(0, len(question_data)):
    question = question_data[i]['text']
    answer = question_data[i]['answer']

    print(question)
    # print(answer)

    # get user input
    user_answer = input("True or False? ").title()

    # check answer
    if user_answer == answer:
        # update score if answer was correct
        clear()
        score += 1
        print(f"Correct!")
    else:
        clear()
        print(f"Nope!!")

print(f"End of questionnaire. Your final score is: {score}")

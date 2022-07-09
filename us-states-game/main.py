from turtle import Turtle, Screen
from pandas import read_csv, DataFrame

screen = Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle(shape=image)

data = read_csv("50_states.csv")

def get_mouse_click_coor(x, y):
    print(x, y)

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name a state below. Keep going until you've named them all!").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    guessed_states.append(answer_state)
    if answer_state in all_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(answer_state)

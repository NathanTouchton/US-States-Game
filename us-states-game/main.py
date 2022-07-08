from turtle import Turtle, Screen

screen = Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle(shape=image)

def get_mouse_click_coor(x, y):
    print(x, y)

answer_state = screen.textinput(title="Name all the states", prompt="Name a state below. Keep going until you've named them all!")

screen.onscreenclick(get_mouse_click_coor)

screen.mainloop()

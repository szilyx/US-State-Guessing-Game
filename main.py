import turtle
from multiprocessing.connection import answer_challenge
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
print(data)
guessed_states = []
while len(guessed_states) < 50:
    def getmouselocation(x,y):
        print(x, y)

    answer_state = screen.textinput(title=f"Guess the State. {len(guessed_states)} already guessed", prompt="Whats the name of the state?").title()

    states = data.state.to_list()
    screen.onscreenclick(getmouselocation)
    if answer_state.title() == "Exit":
        need_to_learn = []
        for i in states:
            if i not in guessed_states:
                need_to_learn.append(i)
        df = pd.DataFrame(need_to_learn)
        df.to_csv("States to learn")
        break

    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_loc = data[data.state == answer_state]
        t.goto(data_loc.x.item(),data_loc.y.item())
        t.write(answer_state)
        guessed_states.append(answer_state)


import turtle
from multiprocessing.connection import answer_challenge

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def getmouselocation(x,y):
    print(x, y)

screen.onscreenclick(getmouselocation)

answer_state = screen.textinput(title="Guess the State", prompt = "Whats the name of the state?")
turtle.mainloop()
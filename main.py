from re import T
from turtle import Turtle, Screen
import turtle

import pandas


screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()

all_states = False

right_guess = 0
length = len(states_data)
guessed_states = []

while len(guessed_states) < length:
    name = screen.textinput(f"{len(guessed_states)}/{length} States Correct", "What's another state name?").title()
    if name == "Exit":
        states_to_learn =[state for state in states_list if state not in guessed_states] 
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("States To Learn.csv")
        break

    if name in states_list and name not in guessed_states:
        
        guessed_states.append(name)
        state_data = states_data[states_data["state"] == name]
        
        x_ = int(state_data.x)
        y_ = int(state_data.y)
        us_turtle = Turtle()
        us_turtle.hideturtle()
   
        us_turtle.penup()
        us_turtle.goto(x_, y_)
        us_turtle.write(state_data.state.item())
       


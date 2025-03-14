from random import choice, randint
from turtle import Turtle, Screen
import turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")

while not user_bet in colors:
    user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = {}

def pick_random_color():
    color = choice(colors)
    while color in turtles:
        color = choice(colors)

    return color

def create_turtle(amount: int, x_pos: int = -230, y_pos: int = -100):
    y_space = 50
    for _ in range(amount):
        y = y_pos + (y_space * _)
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        turtle_color = pick_random_color()
        new_turtle.color(turtle_color)
        new_turtle.goto(x=x_pos, y=y)

        turtles[turtle_color] = new_turtle


def start_race():
    global is_race_on
    is_race_on = True
    turtle_win = ""
    while is_race_on:
        for turtle_color in turtles:
            current_turtle = turtles[turtle_color]
            current_turtle.forward(randint(0, 10))

            if current_turtle.xcor() >= 230:
                is_race_on = False
                turtle_win = turtle_color
                break

    return turtle_win

create_turtle(6)
how_win = start_race()

turtle.TK.messagebox.showinfo(title="The turtle win is:", message=f"{how_win}")

if how_win == user_bet:
    print("Congratulation you win!")
else:
    print(f"To bad, you loser! {how_win} turtle is winner!")

for turtle in turtles:
    turtles[turtle].home()

screen.clear()

win_turtle = Turtle(shape="turtle")
win_turtle.color(how_win)

screen.exitonclick()
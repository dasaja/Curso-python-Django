from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Haz tu apuesta", prompt= "Qué tortuga ganará la carrera? Ingresa un color:")
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#create 6 turtles
for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"¡Has ganado¡ ¡La tortuga {winning_color} es la ganadora¡")
            else:
                print(f"¡Has perdido¡ ¡La tortuga {winning_color} es la ganadora¡")

        #make move
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()


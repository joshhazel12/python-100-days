import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (77, 77, 77), (218, 218, 218), (135, 135, 135), (193, 193, 193), (88, 88, 88), (219, 219, 219), (186, 186, 186), (38, 38, 38), (172, 172, 172), (217, 217, 217), (131, 131, 131), (82, 82, 82), (52, 52, 52), (43, 43, 43), (113, 113, 113), (171, 171, 171), (50, 50, 50), (45, 45, 45), (105, 105, 105), (99, 99, 99)]

tim.hideturtle()
tim.penup()
tim.setx(-225)
tim.sety(-200)
tim.setheading(0)
tim.speed("fastest")


def create_a_row_of_dots():
    for _ in range(9):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.setx(-225)
    tim.setheading(0)


for _ in range(10):
    create_a_row_of_dots()

screen = turtle_module.Screen()
screen.exitonclick()

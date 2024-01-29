from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()

screen.bgcolor("black")
screen.screensize(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((600, 0))
l_paddle = Paddle((-600, 0))



screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()

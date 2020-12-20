import turtle
from random import randint
T = turtle.Turtle()
for i in range(0,20):
    randomx = randint(-400,400)
    randomy = randint(-400,400)
    randomcircle = randint(0,75)
    T.penup()
    T.goto(randomx,randomy)
    T.pendown()
    T.circle(randomcircle)
    T.penup()
    T.goto(0,0)

import turtle
import time
import random
from threading import Thread

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Turtle Game")

score = 0
points = turtle.Turtle()
points.hideturtle()
points.color('Black')
points.penup()
points.goto(-10, 350)
points.write("Score = 0 ", font=("Verdana",  30, "normal"))

a = 10

timer = turtle.Turtle()
timer.hideturtle()
timer.color('Black')
timer.penup()
timer.goto(-10, 400)
timer.write(f"Time = {a} ", font=("Verdana", 30, "normal"))


memduh_turtle = turtle.shape("turtle")
turtle.turtlesize(2)
turtle.color("green")
turtle.speed(0)
turtle.penup()


def func2():
    while a > 0:
        turtle.hideturtle()
        x = random.uniform(-400, 400)
        y = random.uniform(-400, 400)
        turtle.setpos(x, y)
        time.sleep(0.5)
        turtle.showturtle()
        time.sleep(0.5)


def func1():
    global a
    for i in range(10):
        time.sleep(1)
        a = a - 1
        timer.clear()
        timer.write("Time = " + str(a), font=("Verdana", 30, "normal"))
        if a == 0:
            time.sleep(0.5)
            timer.clear()
            timer.write("GAME OVER", font=("Verdana", 30, "normal"))


for m in turtle.pos():
    def addscore(v, b):
        global score
        if a > 0:
            score += 1
            points.clear()
            points.write("Score = " + str(score), font=("Verdana", 30, "normal"))

turtle.onclick(addscore, 1)

if __name__ == '__main__':
    Thread(target=func1).start()
    Thread(target=func2).start()
turtle.done()

import turtle
import random
import time

jason = turtle.Turtle()
ivan = turtle. Turtle()
start = turtle.Turtle()
end = turtle.Turtle

jason.shape("turtle")
jason.color("gold")
jason.speed(20)
jason.penup()
jason.setposition(-310,-150)
jason.pendown()
jason.width(10)
jason.speed(10)


jason.write("--Turtle Graphics Race--",  font=("Times New Roman", 25, "bold"))



#forward, backward, left, right, shape, goto, setposition, penup, pendown, color, clear
ivan.shape("turtle")
ivan.color("red")
ivan.speed(20)
ivan.penup()
ivan.setposition(-310,150)
ivan.pendown()
ivan.width(10)
ivan.speed(10)

start.speed(50)
start.color("green")
start.pensize(5)
start.penup()
start.setposition(-300,400)
start.pendown()
start.rt(90)
start.fd(1000)
start.penup()
start.setposition(300,400)
start.color("red")
start.pendown()
start.fd(1000)

random_forward = [10, 20, 30, 40, 50]
colors = ["green", "red", "yellow"]
for x in range(100):
    jason.fd(random.choice(random_forward))
    jason.color(random.choice(colors))
    ivan.fd(random.choice(random_forward))
    ivan.color(random.choice(colors))
    time.sleep(0.5)


turtle.mainloop()

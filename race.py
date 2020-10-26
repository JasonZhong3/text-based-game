import turtle
import random
import time

jason = turtle.Turtle()
ivan = turtle. Turtle()
start = turtle.Turtle()
end = turtle.Turtle

jason.penup()
jason.setposition(-150, 300)
jason.pendown()
jason.write("--Turtle Graphics Race--",  font=("Times New Roman", 25, "bold"))
jason.shape("turtle")
jason.color("gold")
jason.speed(20)
jason.penup()
jason.setposition(-310,-150)
jason.pendown()
jason.width(10)
jason.speed(10)

#forward, backward, left, right, shape, goto, setposition, penup, pendown, color, clear
ivan.shape("turtle")
ivan.color("red")
ivan.speed(20)
ivan.penup()
ivan.setposition(-310,150)
ivan.pendown()
ivan.width(10)
ivan.speed(10)

start.speed(0)
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

random_forward = [30, 40, 50, 60, 70]
colors = ["green", "red", "yellow"]
for x in range(15):
    jason.fd(random.choice(random_forward))
    jason.color(random.choice(colors))
    ivan.fd(random.choice(random_forward))
    ivan.color(random.choice(colors))
    jason.speed(3)
    ivan.speed(3)
    time.sleep(0.5)
    
    x , y= jason.pos()
    if x > 300:
        start.penup()
        start.setpos(-75, 0)
        start.pendown
        start.write("--You Win--",  font=("Times New Roman", 25, "bold"))

# if either turtle goes fd 600 bits, the race stops and the
# winner is the turtle that  crosses first.

turtle.mainloop()

import turtle

la = turtle.Turtle()
tr = turtle.Turtle()
ho = turtle.Turtle()
su = turtle.Turtle()
no = turtle.Turtle()

turtle.bgcolor("blue")


def wall(side):
    for size in range(4):
        ho.forward(200)
        ho.left(90)


def pane(side):
    for size in range(4):
        ho.forward(12)
        ho.left(90)


def land(side):
    for size in range(2):
        la.forward(800)
        la.right(90)
        la.forward(600)
        la.right(90)


def roof(side):
    for size in range(1):
        no.forward(200)

        no.left(120)
        no.forward(200)
        no.left(120)
        no.forward(200)


def bars(side):
    for size in range(2):
        tr.left(90)
        tr.forward(200)
        tr.left(90)
        tr.forward(15)


def slide(side):
    for size in range(2):
        no.left(89)
        no.forward(50)
        no.left(90)
        no.forward(200)


def door(side):
    for size in range(2):
        no.right(90)
        no.forward(90)
        no.right(90)
        no.forward(60)


def chimney(side):
    for size in range(1):
        tr.left(90)
        tr.forward(90)
        tr.left(90)
        tr.forward(90)
        tr.left(90)
        tr.forward(90)
        tr.left(90)
        tr.forward(90)


def sun(side):
    for size in range(65):
        su.forward(10)
        su.left(7)


def window(side):
    for size in range(4):
        ho.forward(25)
        ho.left(90)


tr.fillcolor("white")
tr.penup()
tr.goto(360, 180)
tr.pendown()
tr.pencolor("white")
tr.begin_fill()
tr.circle(10, 180)
tr.goto(250, 180)
tr.circle(-10, 180)
tr.end_fill()

tr.fillcolor("tan")
tr.penup()
tr.goto(360, 25)
tr.pendown()
tr.pencolor("brown")
tr.begin_fill()
bars(1)
tr.end_fill()

tr.fillcolor("tan")
tr.penup()
tr.goto(280, 25)
tr.pendown()
tr.pencolor("brown")
tr.begin_fill()
bars(1)
tr.end_fill()

tr.fillcolor("brown")
tr.penup()
tr.goto(200, 35)
tr.pendown()
tr.pencolor("brown")
tr.begin_fill()
bars(1)
tr.end_fill()

tr.fillcolor("brown")
tr.penup()
tr.goto(200, 220)
tr.right(90)
tr.pendown()
tr.pencolor("brown")
tr.begin_fill()
bars(1)
tr.end_fill()

tr.fillcolor("gray")
tr.penup()
tr.goto(10, 260)
tr.pendown()
tr.pencolor("gray")
tr.begin_fill()
chimney(1)
tr.end_fill()

tr.fillcolor("black")
tr.penup()
tr.goto(350, 75)
tr.pendown()
tr.pencolor("black")
tr.begin_fill()
tr.right(90)
tr.forward(70)
tr.left(90)
tr.forward(10)
tr.left(90)
tr.forward(70)
tr.left(90)
tr.forward(10)
tr.end_fill()

ho.fillcolor("tan")
ho.penup()
ho.goto(-10, 50)
ho.pendown()
ho.pencolor("black")
ho.begin_fill()
wall(1)
ho.end_fill()

no.fillcolor("brown")
no.penup()
no.goto(100, 140)
no.pendown()
no.pencolor("brown")
no.begin_fill()
door(1)
no.end_fill()

ho.fillcolor("yellow")
ho.penup()
ho.goto(-3, 138)
ho.pendown()
ho.pencolor("black")
ho.begin_fill()
window(1)
ho.end_fill()

ho.penup()
ho.goto(10, 150)
ho.pendown()
ho.pencolor("black")
pane(1)
ho.left(90)
pane(1)
ho.left(90)
pane(1)

ho.fillcolor("yellow")
ho.penup()
ho.goto(163, 163)
ho.pendown()
ho.pencolor("black")
ho.begin_fill()
window(1)
ho.end_fill()

ho.penup()
ho.goto(150, 150)
ho.pendown()
ho.pencolor("black")
pane(1)
ho.left(90)
pane(1)
ho.left(90)
pane(1)

la.fillcolor("yellow")
la.penup()
la.goto(50, 80)
la.pendown()
la.pencolor("black")
la.begin_fill()
la.circle(3, 360)
la.end_fill()

no.fillcolor("red")
no.penup()
no.goto(-10, 247)
no.pendown()
no.pencolor("red")
no.begin_fill()
roof(1)
no.end_fill()

la.fillcolor("green")
la.penup()
la.goto(-400, 60)
la.pendown()
la.pencolor("green")
la.begin_fill()
land(1)
la.end_fill()

no.fillcolor("gray")
no.penup()
no.goto(-200, -300)
no.pendown()
no.pencolor("gray")
no.begin_fill()
slide(1)
no.end_fill()

su.fillcolor("gold")
su.penup()
su.goto(300, 300)
su.pendown()
su.pencolor("orange")
su.begin_fill()
sun(1)
su.end_fill()
su.fillcolor("yellow")
su.penup()
su.goto(300, 380)
su.pendown()
su.pencolor("red")
su.begin_fill()
size = 1
for i in range(200):
    su.forward(size)
    su.right(138)
    size += 1
su.end_fill()

turtle.exitonclick()

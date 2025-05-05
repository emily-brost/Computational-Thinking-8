#setup
import turtle
t = turtle.Turtle()

t.speed(10)
turtle.Screen().bgcolor("light blue")

#variable
height = 300
width = 500
stripe = 50

#blue square
t.goto(-250, 125)
t.color("blue")
t.begin_fill()
t.forward(width)
t.right(90)
t.forward(height)
t.right(90)
t.forward(width)
t.right(90)
t.forward(height)
t.right(90)
t.end_fill()

#vertical stripe
t.goto(-115,125)
t.color("yellow")
t.begin_fill()
t.forward(stripe)
t.right(90)
t.forward(height)
t.right(90)
t.forward(stripe)
t.right(90)
t.forward(height)
t.right(90)
t.end_fill()

#horizontal stripe
t.penup()
t.goto(-250,0)
t.pendown()
t.color("yellow")
t.begin_fill()
t.forward(width)
t.right(90)
t.forward(stripe)
t.right(90)
t.forward(width)
t.right(90)
t.forward(stripe)
t.right(90)
t.end_fill()

turtle.exitonclick()
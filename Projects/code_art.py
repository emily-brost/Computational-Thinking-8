#setup
import turtle
turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.penup()
t.goto(-50, 0)
t.pendown()
t.speed(0)
t.color("seagreen")
colors = ["darkseagreen", "lightgreen", "seagreen", ""]

#rotating shape
for i in range(1000):
    t.color( colors[ i % 3 ] )
    t.forward(100 + i)
    t.left(181)

#end
turtle.exitonclick()
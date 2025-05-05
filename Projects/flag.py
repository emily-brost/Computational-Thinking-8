import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")

#variables
height = 50
length = 500
square = 100

# stripes

# move to stripe 1
t.goto(-250, -100)

# stripe 1
t.color("red")
t.begin_fill()
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, -50)

# stripe 2
t.color("white")
t.begin_fill()
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 3
t.goto(-250, 0)

# stripe 3
t.color("red")
t.begin_fill()
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 4
t.goto(-250, 50)

# stripe 4
t.color("white")
t.begin_fill()
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 5
t.goto(-250, 100)

# stripe 5
t.color("red")
t.begin_fill()
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()


# blue square
t.goto(-250, 100)
t.color("blue")
t.begin_fill()
t.forward(square)
t.left(90)
t.forward(square)
t.left(90)
t.forward(square)
t.left(90)
t.forward(square)
t.left(90)
t.end_fill()

turtle.exitonclick()

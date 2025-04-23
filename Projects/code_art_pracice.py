# #########################################################
# ### SETUP ###
import turtle
# #########################################################

t = turtle.Turtle()
t.penup()
location = -300
t.color("pink")

for i in range(10):
    t.goto(location, 0)
    for i in range(4):
        location += 15
        t.pendown()
        t.forward(50)
        t.left(90)
        t.penup()

# ########################################################
# ### ENDING ###
turtle.exitonclick()
# ########################################################


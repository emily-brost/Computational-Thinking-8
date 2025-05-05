# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite

# Section 2 - Variables
x1 = -200
y1 = 150
x2 = -200
y2 = 50
x3 = -200
y3 = -50
x4 = -200
y4 = -150

# Section 3 - Setup
set_background("spring")
t1 = create_sprite("fish",x1,y1)
t2 = create_sprite("flower",x2,y2)
t3 = create_sprite("soccerball",x3,y3)
t4 = create_sprite("kitten",x4,y4)

# Section 4 - Racing
# t4 is most likely to win
# t3 is least likely to win
# t1, t3, and t4 are random
# t2 is the same every time 
for i in range(50):
	x1 += random.randint(1, 15)
	x2 += 9
	x3 += random.randint(1, 11)
	x4 += random.randint(7, 12)
	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.1)

# Section 5 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("fish wins!")
elif x2 >=x1 and x2 >= x3 and x2 >= x4:
	print("flower wins!")
elif x3 >=x1 and x3 >= x2 and x3 >= x4:
	print("soccerball wins!")
elif x4 >=x1 and x4 >= x2 and x4 >= x3:
	print("kitten wins!")


turtle.exitonclick()

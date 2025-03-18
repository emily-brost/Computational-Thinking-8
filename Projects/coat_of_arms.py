###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("spring")

q1 = codesters.Square(100,100,200, 'purple')
q2 = codesters.Square(100,-100,200, 'thistle')
q3 = codesters.Square(-100,-100,200, 'purple')
q4 = codesters.Square(-100,100,200, 'thistle')

s1 = codesters.Sprite("soccer_ball",-100,100)
s1.set_size(0.75)
s2 = codesters.Sprite("dog2",100,100)
s2.set_size(0.75)
s3 = codesters.Sprite("cardinal",-100,-100)
s3.set_size(0.75)
s4 = codesters.Sprite("art",100,-100)
s4.set_size(0.67)

message1 = codesters.Text("Emily Brost",0,220,"black")

message2 = codesters.Text("Keep your face always toward the sunshine", 0, -215, "black")
message3 = codesters.Text("and shadows will fall behind you", 0, -237, "black")
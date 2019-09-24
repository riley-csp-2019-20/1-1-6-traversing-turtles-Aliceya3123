#   a115_buggy_image.py
import turtle as trtl

spiderbody= trtl.Turtle()
spiderbody.pensize(40)
spiderbody.circle(20)
w = 8
length = 90
circle = 380 / w
spiderbody.pensize(5)
spiderlegs = 0
while (spiderlegs < w):
  spiderbody.goto(1,25)
  spiderbody.setheading(circle*spiderlegs)
  spiderbody.forward(length)
  spiderlegs = spiderlegs+ 1
spiderbody.hideturtle()


body.goto(1,25)
body.pencolor("red")
body.circle(8)

body.goto(1,27)
body.pencolor
body.circle(8)


wn = trtl.Screen()
wn.mainloop()
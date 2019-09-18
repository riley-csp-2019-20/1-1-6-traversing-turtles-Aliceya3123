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
  spiderbody.goto(0,0)
  spiderbody.setheading(circle*spiderlegs)
  spiderbody.forward(length)
  spiderlegs = spiderlegs+ 1
spiderbody.hideturtle()
wn = trtl.Screen()
wn.mainloop()
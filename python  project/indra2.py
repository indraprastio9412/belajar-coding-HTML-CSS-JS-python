import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen().bgcolor("black")
t.speed(0)
n=70
h=0
for i in range(100):
	c=colorsys.hsv_to_rgb(h,1,1)
	h+=1/n
	t.color(c)
	t.left(1)
	t.fd(1)
	t.hideturtle()
	for j in range (2):
		t.left(2)
		t.circle(100)



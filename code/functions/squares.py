import turtle
crush = turtle.Turtle()
apple = turtle.Turtle()
apple.color("red")
# docstring
"""
Draw a square using the turtle passed into qwerty
"""
def square(qwerty,x,y,w,color,heading):
   qwerty.penup()
   qwerty.goto(x,y)
   qwerty.color(color)
   qwerty.pendown()
   for i in range(4):
     qwerty.forward(w)
     qwerty.left(90)

wn = turtle.Screen()

def ngon(qwerty,x,y,sides,w,color,heading):
   qwerty.penup()
   qwerty.goto(x,y)
   qwerty.color(color)
   qwerty.pendown()
   qwerty.setheading(float(heading))
   for i in range(sides):
     qwerty.forward(w)
     qwerty.left(360/sides)

ngon(apple,-50,-50,10,40,"turquoise",47)
wn.exitonclick()

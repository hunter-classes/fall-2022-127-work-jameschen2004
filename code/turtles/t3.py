import turtle
wn = turtle.Screen()

drawer = turtle.Turtle()
sides = int(input("How many sides are in your shape?"))
for i in range(sides):
  drawer.forward(50)
  angle = 360 / sides
  drawer.right(angle)

wn.exitonclick()
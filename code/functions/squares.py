import turtle
crush = turtle.Turtle()
apple = turtle.Turtle()
apple.color("red")
def square(qwerty):
 for i in range(4):
   qwerty.forward(50)
   qwerty.right(90)

wn = turtle.Screen()

square(apple)
square(crush)
wn.exitonclick()
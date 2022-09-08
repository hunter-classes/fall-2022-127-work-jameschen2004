# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# I have created a hexagon function, followed by a n-gon function with the use of the turtle module

import turtle
wn = turtle.Screen()
hexagongle = turtle.Turtle()
decagongle = turtle.Turtle()
def hexagon(squirtle,x,y,color,width,heading):
  squirtle.penup()
  squirtle.goto(x,y)
  squirtle.color(color)
  squirtle.pendown()
  squirtle.setheading(heading)
  for i in range (6):
     squirtle.forward(width)
     squirtle.left(60)


hexagon(hexagongle,-50,-50,"pink",60,45)

def ngon(turtwig,numsides,x,y,color,width,sidelen):
   turtwig.penup()
   turtwig.goto(x,y)
   turtwig.color(color)
   turtwig.pendown()
   turtwig.width(width)
   for i in range (numsides):
      turtwig.forward(sidelen)
      turtwig.left(360 / numsides)


ngon(decagongle,10,50,-50,"turquoise",5,30)
wn.exitonclick()
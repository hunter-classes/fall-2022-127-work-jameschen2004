# Fall 2022 - 127 - Work
# Name: James Chen

# GitHub username: jameschen2004

# this is my solution to exercise 4.7

import turtle
wn = turtle.Screen()

drunk_pirate = turtle.Turtle()
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
 drunk_pirate.left(angle)
 drunk_pirate.forward(100)

print("The drunk pirate's current heading is", drunk_pirate.heading)
wn.exitonclick()
#Author: Molena Nguyen

import turtle
wn = turtle.Screen()
wn.bgcolor("#E0FFFF")
turtle1 = turtle.Turtle()
turtle1.shape("arrow")
turtle2 = int(input())
turtle1.speed(10)
turtle3 = int(input("Pick a number:  " ))
if turtle3 == 1:
    for a_color in ["black", "white", "red", "lime", "blue"]:
        turtle1.color(a_color)
        for i in range(turtle3):
            turtle1.right(40)
            turtle1.forward(50)
            turtle1.stamp()
            turtle1.backward(turtle3)
            turtle3.dot()
            i += 1
elif turtle3 == 2:
    for a_color in ["yellow", "aqua", "magenta", "silver", "gray"]:
        turtle1.color(a_color)
        for i in range(turtle3):
            turtle1.right(40)
            turtle1.forward(50)
            turtle1.stamp()
            turtle1.backward(turtle3)
            turtle1.dot()
            i += 1
else:
   for a_color in ["maroon", "olive", "green", "purple", "teal", "navy"]:
        turtle1.color(a_color)
        for i in range(turtle3):
            turtle1.right(180)
            turtle1.forward(50)
            turtle1.stamp()
            turtle1.backward(turtle3)
            turtle1.dot()
            i +=1
wn.exitonclick()

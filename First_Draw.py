#Author: Molena Nguyen

import turtle
wn = turtle.Screen()
wn.bgcolor("#E0FFFF")
turtle1 = turtle.Turtle()
turtle1.shape("circle")
turtle2 = int(input())
for a_color in ["black", "white", "red", "lime", "blue", "yellow", "aqua", "magenta", "silver", "gray", "maroon", "olive", "green", "purple", "teal", "navy"]:
    turtle1.color(a_color)
    for i in range(turtle2):
        turtle1.right(10)
        turtle1.forward(40)
        turtle1.stamp()
        turtle1.backward(turtle2)
        turtle1.dot()
        i +=1
wn.exitonclick()

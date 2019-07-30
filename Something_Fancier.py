#Author: Thy H. Nguyen

import turtle
wn = turtle.Screen()
wn.bgcolor("#E0FFFF")
mom = turtle.Turtle()
mom.shape("arrow")
thuy = int(input())
mom.speed(10)
thy = int(input("Pick a number:  " ))
if thy == 1:
    for comi in ["black", "white", "red", "lime", "blue"]:
        mom.color(comi)
        for i in range(thy):
            mom.right(40)
            mom.forward(50)
            mom.stamp()
            mom.backward(thy)
            mom.dot()
            i += 1
elif thy == 2:
    for comi in ["yellow", "aqua", "magenta", "silver", "gray"]:
        mom.color(comi)
        for i in range(thy):
            mom.right(40)
            mom.forward(50)
            mom.stamp()
            mom.backward(thy)
            mom.dot()
            i += 1
else:
   for comi in ["maroon", "olive", "green", "purple", "teal", "navy"]:
        mom.color(comi)
        for i in range(thy):
            mom.right(180)
            mom.forward(50)
            mom.stamp()
            mom.backward(thy)
            mom.dot()
            i +=1
wn.exitonclick()

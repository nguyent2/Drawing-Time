#Author: Molena Nguyen

import turtle
wn = turtle.Screen()
wn.bgcolor("#E0FFFF")
turtle1 = turtle.Turtle()
turtle1.color("#0000CD")
turtle1.shape("circle")
turtle2 = int(input())
i=1
while i < turtle2:
    turtle1.right(10)
    turtle1.forward(100)
    turtle1.stamp()
    turtle1.backward(turtle2)
    turtle1.dot()
    i +=1
wn.exitonclick()

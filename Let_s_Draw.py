#Author: Thy H. Nguyen

import turtle
wn = turtle.Screen()
wn.bgcolor("#E0FFFF")
mom = turtle.Turtle()
mom.color("#0000CD")
mom.shape("circle")
thy = int(input())
i=1
while i < thy:
    mom.right(10)
    mom.forward(100)
    mom.stamp()
    mom.backward(thy)
    mom.dot()
    i +=1
wn.exitonclick()

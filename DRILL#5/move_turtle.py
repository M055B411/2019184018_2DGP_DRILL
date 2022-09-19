import turtle

def forward_turtle():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def backward_turtle():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def toright_turtle():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def toleft_turtle():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def reset_turtle():
    turtle.stamp()
    turtle.reset()


turtle.shape("turtle")
turtle.onkey(forward_turtle,'w')
turtle.onkey(backward_turtle,'s')
turtle.onkey(toright_turtle,'d')
turtle.onkey(toleft_turtle,'a')
turtle.onkey(reset_turtle,'Escape')
turtle.listen()

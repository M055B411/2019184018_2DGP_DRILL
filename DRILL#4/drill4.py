import turtle

sqare = 4
while sqare > 0:
    turtle.forward(500)
    turtle.left(90)
    sqare -= 1

vert = 4
while vert > 0:
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.backward(500)
    turtle.right(90)
    vert -= 1

turtle.forward(100)
turtle.left(90)

hori = 4
while hori > 0:
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.backward(500)
    turtle.right(90)
    hori -= 1

turtle.forward(100)
turtle.right(90)

turtle.exitonclick()

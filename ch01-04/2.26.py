import turtle
cx1,cy1=eval(input("What are the coordinates for the center your circle:"))
radius= eval(input("What is the radius:"))

turtle.showturtle()
turtle.penup()
turtle.goto(cx1,(cy1-radius))
turtle.pendown()
turtle.circle(radius)
turtle.penup()
area = 3.14 * radius ** 2
turtle.write(area)


turtle.done()
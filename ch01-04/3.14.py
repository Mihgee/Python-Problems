import turtle as t

r = eval(input("Enter Radius:  "))
t.speed(10)
x =t.xcor()


t.penup()
t.backward(200)
t.pendown()
t.pensize(11)

t.color("blue")
t.circle(r)

t.penup()
t.forward(x + r * 2.5)
t.pendown()

t.color("black")
t.circle(r)

t.penup()
t.forward(x + r * 2.5)
t.pendown()

t.color("red")
t.circle(r)

t.penup()
t.backward(x + r * 4.75)
t.left(-90)
t.forward(x + 20)
t.pendown()

t.color("yellow")
t.circle(r)

t.penup()
t.left(90)
t.forward(x + r * 2.5)
t.left(-90)
t.forward(x)
t.pendown()

t.color("green")
t.circle(r)
t.done()
import turtle as t
t.Screen().setworldcoordinates(-550,-550,550,550)
t.speed(0)

x= -500
y= 500
size = 1000/8

t.up()
t.goto(x,y)

for i in range(8):
    t.down()
    for j in range(8):
        if (i%2==0 and j%2!=0) or (i%2!=0 and j%2 ==0):
            t.begin_fill()
        for k in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()
        t.forward(size)
    y -= size
    t.up()
    t.goto(x,y)
t.hideturtle()
t.done()
import turtle as t

def main():
    drawChessboard(-260, -20, -120, 120)
    drawChessboard(20, 260, -120, 120)

    t.hideturtle()
    t.done()


def drawChessboard(startx, endx, starty, endy):
    t.pensize(3)
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.color("black")

    for i in range(4):
        t.forward(240)
        t.left(90)


    drawMultipleRectangle(startx, endx, starty, endy)
    drawMultipleRectangle(startx + 30, endx, starty + 30, endy)


def drawMultipleRectangle(startx, endx, starty, endy):
    t.color("black")
    for j in range(starty, endy, 60):
        for i in range(startx, endx, 60):
            fillRectangle(i, j)


def fillRectangle(i, j):
    t.penup()
    t.goto(i, j)
    t.pendown()
    t.begin_fill()
    for k in range(4):
        t.forward(30)
        t.left(90)
    t.end_fill()

main()
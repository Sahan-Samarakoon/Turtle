import turtle
t = turtle.Pen()
def star(size, filled):
    if filled == True:
        t.begin_fill()
        t.color(0.9, 0.75, 0)
    for x in range(1,19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()

star(100, True)
t.color(0, 0, 0)
star(100, False)
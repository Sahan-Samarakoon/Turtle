from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
mj = canvas.create_polygon(10, 10, 40, 30, 10, 50)

def moving_triangle(event):
    if event.keysym == 'W':
        canvas.move(mj, 0, -3)
    elif event.keysym == 'S':
        canvas.move(mj, 0, 3)
    elif event.keysym == 'A':
        canvas.move(mj, -3, 0)
    else:
        canvas.move(mj, 3, 0)

canvas.bind_all('<KeyPress-S>', moving_triangle)
canvas.bind_all('<KeyPress-W>', moving_triangle)
canvas.bind_all('<KeyPress-A>', moving_triangle)
canvas.bind_all('<KeyPress-D>', moving_triangle)


from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
mj = canvas.create_polygon(10, 10, 40, 30, 10, 50)

def moving_triangle(event):
    if event.keysym == 'w':
        canvas.move(mj, 0, -3)
    elif event.keysym == 's':
        canvas.move(mj, 0, 3)
    elif event.keysym == 'a':
        canvas.move(mj, -3, 0)
    else:
        canvas.move(mj, 3, 0)

canvas.bind_all('<KeyPress-s>', moving_triangle)
canvas.bind_all('<KeyPress-w>', moving_triangle)
canvas.bind_all('<KeyPress-a>', moving_triangle)
canvas.bind_all('<KeyPress-d>', moving_triangle)


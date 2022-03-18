import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, height=400, width=500)
canvas.pack()
canvas.create_polygon(10, 10, 30, 10, 10, 50)
for x in range(0, 60):
    canvas.move(1, 5, 0)
    canvas.update()
    time.sleep(0.05)
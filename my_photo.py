from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, width=1000, height=500)
canvas.pack()
my_image = PhotoImage(file='d:\\Personal\\Sahan\\waddek.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)
for x in range(0,250):
    canvas.move(1, 2, 0)
    canvas.update()
    time.sleep(0.05)

for y in range(0, 105):
    canvas.move(1, 0, 2)
    canvas.update()
    time.sleep(0.05)

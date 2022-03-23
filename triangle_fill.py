import random
from tkinter import *
tk = Tk()
w = 400
h = 400
canvas = Canvas(tk, width=w, height=h)
canvas.pack()
color_list = ['Orange', 'Red', 'Yellow', 'Green', 'Blue', 'Purple', 'White']
def random_triangle():
    p1 = random.randrange(w)
    p2 = random.randrange(h)
    p3 = random.randrange(w)
    p4 = random.randrange(h)
    p5 = random.randrange(w)
    p6 = random.randrange(h)
    random_color = random.choice(color_list)
    canvas.create_polygon(p1, p2, p3, p4, p5, p6, fill=random_color, outline="")

for x in range(0,100):
    random_triangle()





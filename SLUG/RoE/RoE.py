import tkinter
from tkinter import *
top = tkinter.Tk()

def helloCallBack():
    print('Hello World')
    return

C = tkinter.Canvas(top, bg = 'white', height = 250, width = 300)

coord = 10,50,240,210
arc = C.create_arc(coord, start = 0, extent = 150, fill = 'red', outline = 'red')

coord = 240/3,210/1.8
text = C.create_text(coord, text = 'Hello World', activefill = 'blue')
coord = 240,210
text = C.create_text(coord, text = 'World Hello', activefill = 'green')

root = Tk()

def key(event):
    print('pressed', repr(event.char))
    return

def callback(event):
    frame.focus_set()
    print('clicked at', event.x, event.y)
    return

frame = Frame(root, width = 100, height = 100)
frame.bind('<Key>', key)
frame.bind('<Button-1>', callback)
frame.pack()
root.mainloop()

C.pack()
top.mainloop()

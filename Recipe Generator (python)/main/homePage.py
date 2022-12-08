from cProfile import label
from cgitb import text
from distutils import command
from email.headerregistry import ContentDispositionHeader
from re import L
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

root = Tk()

frame = Frame(
    root
    )
frame.pack(expand=True, fill=BOTH)

canvas=Canvas(
    frame,
    bg='#4A7A8C',
    width=500,
    height=400
    )

vertibar=Scrollbar(
    frame,
    orient=VERTICAL
    )
vertibar.pack(side=RIGHT,fill=Y)
vertibar.config(command=canvas.yview)

horibar=Scrollbar(
    frame,
    orient=HORIZONTAL
    )
horibar.pack(side=BOTTOM,fill=X)
horibar.config(command=canvas.xview)
canvas.config(
    xscrollcommand=horibar.set, 
    yscrollcommand=vertibar.set
    )
#canvas.bind('<configure>', canvas.configure(scrollregion= canvas.bbox('all')))
fmz = Frame(canvas)    
canvas.create_window((0,0), window=fmz, anchor=NW)

for i in range(20):
    label = Label(fmz, text='sdnkjandkjn').pack()
root.mainloop()
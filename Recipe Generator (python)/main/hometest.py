from email.mime import image
from tkinter import *


#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry
win.geometry("700x350")

#Set the default color of the window
win.config(bg='#aad5df')

#Create a Label to display the text
label=Label(win, text= "Hello dsjaljd;sWorld!",font= ('Helvetica 18 bold'), background= 'white', foreground='purple1')
label.pack(pady = 50)


#Return and print the width of label widget
width = label.winfo_height()
print("The width of the label is:", width, "pixels")

win.mainloop()

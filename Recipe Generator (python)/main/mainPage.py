from ast import Lambda, arguments
from cProfile import label
from cgitb import text
from cmath import e
from ctypes import resize
from dis import Instruction
from distutils.command.config import config
from distutils.command.sdist import sdist
from email.mime import image
from functools import cache
from itertools import count
from msilib.schema import Class, File
from os import stat
from pickle import FRAME, GLOBAL
from re import I, L, T, search
from sre_parse import State
from struct import pack
from textwrap import fill
import this
from threading import Timer
from time import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from turtle import ScrolledCanvas, color, left, onclick, right, up, width
from xml.sax import SAXNotSupportedException
from PIL import ImageTk, Image
from dataclasses import dataclass
from os import remove
import  psycopg2
import  psycopg2.extras

root = tk.Tk()
root.configure(background='#28292e')
fav_btn = Button
home_btn = Button
fav_border = Frame
home_border = Frame
search_frame = Frame()
srch_bar = Text
srch_btn = Button
my_canvas = Canvas
canvas = Canvas
myLabel = Label
fmz = Frame()
recipe_frame = LabelFrame()
title = Label
my_image = image
my_icon = ImageTk
rec_icon = ImageTk
back_icon = ImageTk
timer_icon   = ImageTk
hat_icon = ImageTk
fav_icon = ImageTk
detail_frame = Frame
resized_image = image
ingridients = StringVar()

recipeTxt = '1) Ayurveda mentions \bnsadnjna\nnjadn\nas\na\na\na\na\n\naa\naa\naa\naa\naa\naan\naaathat Curd is hot in nature as contrary to the popular belief that curd is cooling in nature. I was told by my ayurvedic doctor to stop having curd rice for some time as I was having an aggravated pitta dosha – meaning heat imbalance in the body and mind.\n2) Curd rice is good for people having vata dosha imbalance. people with vitiated pitta dosha or kapha dosha should avoid having curd. Buttermilk made from churning butter is a good option for these folks.\n3) Curd is Heavy to digest.\n4) With curd, it is better to have curd which is Well set and fresh. avoid having curd which has become too sour.\n5) Best to use homemade curd – for this curd rice recipe and also when making any dish with curd.\n6) Avoid having curd in the night As it increases mucus.\n7) Do not heat curd as it destroys the friendly bacteria present in it.8) Almond yogurt, coconut milk yogurt or cashew yogurt can be used instead of dairy curd.\n9) You can also add raw mango pieces.\nCurd rice can be just had plain or can be served after a South Indian meal.'

# Database connection 
mydb = psycopg2.connect("dbname=RecipeGen user=postgres password=1234")
cursor = mydb.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Disable Buttons

def dis_home():
    global home_btn,home_border
    home_border = Frame(toolbar_frame, background="lightgrey")
    home_border.grid(row=0, column=2, padx=1)
    home_btn(home_border, width=15,bd=0, foreground="#fac031",activebackground='#28292e',background='#28292e',relief=SOLID, text='Home',command=active_home_button).grid(row=0, column=0, padx=1, pady=1)
# Ative button



def active_search_button():
    srch_bord = Frame(search_frame, width=20, relief=SOLID, bd=0 ,background='#fac031')
    srch_bord.grid(row=0,column=1, padx=20, pady=1)
    srch_btn = Button(srch_bord,text="Search",activebackground='#fac031', width=20, relief=SOLID, bd=0 ,background='#28292e',foreground='white',command=search).grid(row=0,column=0, padx=1, pady=1)

def dis_search():
    srch_bord = Frame(search_frame, width=20, relief=SOLID, bd=0 ,background='lightgrey')
    srch_bord.grid(row=0,column=1, padx=20, pady=1)
    srch_btn = Button(srch_bord,text="Search",activebackground='#fac031', width=20, relief=SOLID, bd=0 ,background='#28292e',foreground='#fac031',command=search).grid(row=0,column=0, padx=1, pady=1)
    

# active recipe effect
def active_recipe(self):
    title = Label(recipe_frame, text='My ')




# Create Main Frame
main_frame = Frame(root,background='#28292e')
main_frame.pack(fill=BOTH, expand=1)

# Creating Header
border_color = Frame(main_frame, background="#fac031")
icon = Image.open("assets/icon.jpg")
rsz = icon.resize((100,100),Image.ANTIALIAS)
icon = ImageTk.PhotoImage(rsz)
icon_lbl = Label(border_color,background='#28292e',image=icon, anchor=W).grid(column=0,row=0,pady=1,padx=0,ipadx=4, ipady=4)
header_label = Label(border_color,background='#28292e',foreground='white', text='  SMARTChief', font=("Times",32,'bold'), bd=0, width=50, anchor=W)
header_label.grid(column=1,row=0,pady=1, ipadx=10, ipady=31)
border_color.pack(side=TOP, fill=X,pady=2)


# Creating Toolbar
toolbar_frame = Frame(main_frame, background="#28292e")
toolbar_frame.pack(side=TOP, fill=X)
toolbar_label1 = Label(toolbar_frame, text='     HEY, ', font=("Times",28,'bold'), bd=0, width=7 , anchor=W,background='#28292e',foreground='white')
toolbar_label1.grid(row=0 , column=0,padx=5)
#toolbar_label.pack(ipadx=10, ipady=10, fill=X)

toolbar_label2 = Label(toolbar_frame, text='USER', font=("Times",28,'bold'), bd=0, width=23, anchor=W, foreground="#d00258",background='#28292e')
toolbar_label2.grid_configure(row=0, column=1, pady=10,padx=1)

# adding border to buttons

home_border = Frame(toolbar_frame, background="lightgrey")
home_border.grid(row=0, column=2,padx=1)

count = 0
def active_home_button():
    global home_btn,home_border,count   
    dis_search()
    if count== 0:
        home()
        count = 1
    else: re_home()
    home_border = Frame(toolbar_frame, background="#fac031")
    home_border.grid(row=0, column=2,padx=1)
    home_btn(home_border, width=15,bd=0, foreground="white",activebackground='#28292e',background='#28292e',relief=SOLID, text='Home',command=re_home).grid(row=0, column=0, padx=1, pady=1)

def re_home():
    dis_search()
    global my_icon,canvas,fmz,recipe_frame,timer_icon,hat_icon,fav_icon

    for widget in canvas.winfo_children():
        widget.destroy()

    total_recipe = []
    cursor.execute("SELECT * FROM recipe;")
    for record in cursor.fetchall():
        total_recipe.append(record[0])
    
    Time = Image.open("assets/timer.png")
    tim_rsz = Time.resize((20,20),Image.ANTIALIAS)
    timer_icon = ImageTk.PhotoImage(tim_rsz)

    #hat image 
    hat = Image.open("assets/hat.jpg")
    hat_rsz = hat.resize((20,20),Image.ANTIALIAS)
    hat_icon = ImageTk.PhotoImage(hat_rsz)

    #matched image
    fav = Image.open("assets/right.png")
    fav_rsz = fav.resize((25,25),Image.ANTIALIAS)
    fav_icon = ImageTk.PhotoImage(fav_rsz)


    fmz = Frame(canvas,background='#28292e')
    canvas.create_window((0,0), window=fmz, anchor=NW)
    
    row = 0 
    col = 0
    x = 0
    y = 0
    for i in total_recipe:
        cursor.execute('select * from  public.recipe where "Recipe_id" = %s;',(i,))
        for record in cursor.fetchall():
            id = record[0]
            title_txt = record[1]
            time = record[4]
            diff = record[5]

        recipe_frame = LabelFrame(fmz, background='#fac031',width=250, height=200,bd=0,labelanchor=W)
        # importing Image
        my_image = Image.open("assets/"+title_txt+".jpg")
        # Resize image
        resized_image = my_image.resize((210,180),Image.ANTIALIAS)
        my_icon = ImageTk.PhotoImage(resized_image)

        myLabel = tk.Button(recipe_frame,bd=0,relief='solid',command=lambda k=i :get_recipe(k))
        myLabel.grid(column=0,row=0)
        myLabel.image = my_icon
        myLabel['image'] = my_icon
        detail = LabelFrame(recipe_frame, background='#fac031',bd=0)
        title = Label(recipe_frame, text=title_txt ,anchor=W,background='#fac031', font='Times 11',foreground='black',bd=0,height=2,width=24)
        timer = Label(detail,image=timer_icon, background='#fac031',anchor=W)
        time_txt = Label(detail,background='#fac031',foreground='black',width=6,text=time,font='Times 10',anchor=W)
        hatt = Label(detail,image=hat_icon, background='#fac031',anchor=W)
        time_txt2 = Label(detail,background='#fac031',foreground='black',width=6, text=diff,font='Times 10',anchor=W)
        favv = Label(detail,image=fav_icon, background='#fac031',anchor=W)
        matched = Label(detail,background='#fac031',foreground='black',text='null',font='Times 10',anchor=W)
        recipe_frame.grid(row=row, column=col, padx=40, pady=40)
        detail.grid()
        timer.grid(row=1,column=0)
        time_txt.grid(row=1,column=1,padx=1)
        hatt.grid(row=1,column=2)
        time_txt2.grid(row=1,column=3,padx=1)
        favv.grid(row=1,column=4,padx=1)
        matched.grid(row=1,column=5,padx=1)
        title.grid(row=2,pady=2)
        col = col+1
        if col == 3:
            col = 0
            row = row+1

    root.update()
    canvas.configure(scrollregion=(0,0,fmz.winfo_width(),fmz.winfo_height()))
    
    
#fav_btn(fav_border, width=15, bd=0, foreground="#fac031",relief=SOLID,activebackground='#28292e', text='Favourite',background='#28292e', command=active_fav_button,padx=10).grid(column=0, row=0, padx=1, pady=1)
home_btn(home_border,bd=0, foreground="#fac031",relief=SOLID,activebackground='#28292e', text='Home',background='#28292e',command=re_home).grid(row=0, column=0, padx=1, pady=1)

# Back button Fun
def get_back():
    global main_frame,detail_frame,instuction,result
    main_frame.pack(fill=BOTH, expand=1)
    result_frame.destroy()
    fmzz.destroy()
    inst_canv.destroy()
    result.destroy()
    detail_frame.destroy()
    instuction.destroy()
    yscroll.destroy()
    xscroll.destroy()





# Create Result Page
def get_recipe(idz):
    global main_frame,back_icon,result_frame,rec_icon,detail,detail_frame,fmzz,instuction,inst_canv,result,yscroll,xscroll
    main_frame.pack_forget()
    result_frame = Frame(root,background='#28292e')

    cursor.execute('select * from  public.recipe where "Recipe_id" = %s;',(idz,))
    for record in cursor.fetchall():
        id = record[0]
        title_txt = record[1]
        ing_txt = str(record[2])
        ing_txt= ing_txt.split()
        inst_txt = str(record[3])
        inst_txt = inst_txt.replace('\\n', '\n').replace('\\t', '\t')
        #inst_txt = inst_txt.replace()
        time = record[4]
        diff = record[5]

    all_ing = ""
    for ing in ing_txt:
        all_ing = all_ing+ing+"\n"

    print(inst_txt)
    # back button
    heading = Frame(result_frame,background='#28292e')
    back = Image.open("assets/back.png")
    back_rsz = back.resize((100,100),Image.ANTIALIAS)
    back_icon = ImageTk.PhotoImage(back_rsz)
    backlbl = Button(heading,background='#28292e',anchor=W, image=back_icon,relief='solid',bd=0,overrelief='solid',activebackground='#28292e',command=get_back)
    backlbl.grid(pady=10,padx=10,column=0, row=0)

    header_label = Label(heading,background='#28292e',foreground='white', text=title_txt, font=("Times",32,'bold'), bd=0, width=50,anchor=W)
    header_label.grid(pady=10,padx=10,column=1,row=0)
    heading.pack(fill=X,expand=1)

    result = Frame(result_frame,background='#28292e',bd=0)
    my_image = Image.open("assets/"+title_txt+".jpg")
    resized_image = my_image.resize((300,250),Image.ANTIALIAS)
    rec_icon = ImageTk.PhotoImage(resized_image)
    recipe_icon = Label(result,image=rec_icon,bd=0,anchor=NW,justify=LEFT).grid(row=0,column=0 ,padx=50,pady=20)
    ingridients_label = Label(result,background='#28292e')
    ing_title = Label(ingridients_label,text = 'INGRIDIENTS :',font='Times 16',bd=0,anchor=NW,justify=LEFT,background='#28292e',foreground='#fac031',width=35).grid(row=0,column=0,padx=0,pady=5 )
    ings = Label(ingridients_label,text = all_ing,font='Times 14',bd=0,anchor=NW,justify=LEFT,background='#28292e',foreground='white',height=10,width=40)
    ingridients_label.grid(row=0,column=1 ,padx=40,pady=10,ipadx=0,ipady=0)
    ings.grid(row=1,column=0 )
    result.pack(side=LEFT,fill=X,expand=1)
    result_frame.pack(pady=0)

    detail_frame = Frame(root,background='#28292e',bd=0)
    detail_frame.pack()
    detail = Label(detail_frame,background='#28292e',foreground='#fac031', text='INSTRUCTIONS', font='Times 18', bd=0, width=50,anchor=NW,justify=LEFT).pack(anchor=NW,padx=40)
    instuction = LabelFrame(root,background='#28292e',bd=0)
    inst_canv = Canvas(instuction,bd=0,background='#28292e')
    yscroll=ttk.Scrollbar(root,orient=VERTICAL)
    xscroll=ttk.Scrollbar(root,orient=HORIZONTAL,)
    inst_canv.config(yscrollcommand=yscroll.set,xscrollcommand=xscroll.set,background='#28292e',bd=0)
    yscroll.configure(command=inst_canv.yview)
    xscroll.configure(command=inst_canv.xview)
    #inst_canv.config(scrollregion=(0,0,root.winfo_height(),root.winfo_width))
    inst_canv.pack(expand=1,side=LEFT,fill=BOTH)
    yscroll.pack(fill=Y,side=RIGHT)
    xscroll.pack(fill=X,side=BOTTOM)
    inst_canv.bind('<configure>', inst_canv.configure(scrollregion= inst_canv.bbox('all')))
    fmzz = Frame(inst_canv,background='#28292e',bd=0)
    inst_canv.create_window((0,0), window=fmzz, anchor=NW)
    instuction.pack(anchor=NW,padx=40,pady=10,expand=1,fill=BOTH) 
    inst_canv.pack(expand=1,fill=BOTH)
    detail_final = Label(fmzz,height=15,width=100,background='#28292e',foreground='white', text=inst_txt, font='Times 14', bd=0,anchor=NW,justify=LEFT,pady=10,relief='solid')
    inst_canv.pack()
    detail_final.pack(anchor=NW,fill=BOTH,expand=1)
    root.update()
    inst_canv.configure(scrollregion=(0,0,detail_final.winfo_width(),detail_final.winfo_height()))
    print(fmzz.winfo_height())
    #detail_frame.pack(side=LEFT,anchor=NW,fill=BOTH,expand=1)
    



    
# Create Home Page

def home():
    global main_frame,myLabel,my_icon,srch_bar,search_frame,srch_btn,timer_icon,hat_icon,fav_icon,favs_icon,favs,canvas,recipe_frame,vertibar,canvas2
    
    total_recipe = []
    cursor.execute("SELECT * FROM recipe;")
    for record in cursor.fetchall():
        total_recipe.append(record[0])

    print(total_recipe)
    # Creating search Frame, button
    search_frame = Frame(main_frame,background='#28292e',bd=0)
    srch_bar = Entry(search_frame,width=80,font='arial 10',background='grey',foreground='white',textvariable=ingridients).grid(row=0 ,column=0)
    srch_bord = Frame(search_frame, width=20, relief=SOLID, bd=0 ,background='#fac031')
    srch_bord.grid(row=0,column=1, padx=20, pady=1)
    srch_btn = Button(srch_bord,text="Search",activebackground='#fac031', width=20, relief=SOLID, bd=0 ,background='#28292e',foreground='#fac031',command=search).grid(row=0,column=0, padx=1, pady=1)
    search_frame.pack()
    # Create canvas
    canvas=Canvas(main_frame,width=500,height=400,bd=0,scrollregion=(0,0,1200,1200),)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)
    # Create second frame inside canvas
    fmz = Frame(canvas,background='#28292e')
    canvas.create_window((0,0), window=fmz, anchor=NW)
    
        
    # Create scrollbar and configure
    vertibar=ttk.Scrollbar(main_frame,orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=500,height=400,bd=0)
    canvas.config(yscrollcommand=vertibar.set,background='#28292e')
    canvas.bind('<configure>', canvas.configure(scrollregion= canvas.bbox('all')))
    
    Time = Image.open("assets/timer.png")
    tim_rsz = Time.resize((20,20),Image.ANTIALIAS)
    timer_icon = ImageTk.PhotoImage(tim_rsz)
    

    #hat image 
    hat = Image.open("assets/hat.jpg")
    hat_rsz = hat.resize((20,20),Image.ANTIALIAS)
    hat_icon = ImageTk.PhotoImage(hat_rsz)

    #matched image
    fav = Image.open("assets/right.png")
    fav_rsz = fav.resize((25,25),Image.ANTIALIAS)
    fav_icon = ImageTk.PhotoImage(fav_rsz)

    #fav image
    favs = Image.open("assets/fav.png")
    favs_rsz = favs.resize((18,18),Image.ANTIALIAS)
    favs_icon = ImageTk.PhotoImage(favs_rsz)
    
    
    row = 0 
    col = 0
    x = 0
    y = 0
    r = 0

    for i in total_recipe:
        cursor.execute('select * from  public.recipe where "Recipe_id" = %s;',(i,))
        for record in cursor.fetchall():
            id = record[0]
            title_txt = record[1]
            time = record[4]
            diff = record[5]
    
        recipe_frame = LabelFrame(fmz, background='#fac031',width=250, height=200,bd=0,labelanchor=W)
        # importing Image
        my_image = Image.open("assets/"+title_txt+".jpg")
        # Resize image
        resized_image = my_image.resize((210,180),Image.ANTIALIAS)
        my_icon = ImageTk.PhotoImage(resized_image)

        myLabel = tk.Button(recipe_frame,bd=0,relief='solid',command=lambda k=i :get_recipe(k))
        myLabel.grid(column=0,row=0)
        myLabel.image = my_icon
        myLabel['image'] = my_icon
        detail = LabelFrame(recipe_frame, background='#fac031',bd=0)
        title = Label(recipe_frame, text=title_txt ,anchor=W,background='#fac031', font='Times 11',foreground='black',bd=0,height=2,width=24)
        timer = Label(detail,image=timer_icon, background='#fac031',anchor=W)
        time_txt = Label(detail,background='#fac031',foreground='black',width=6,text=time,font='Times 10',anchor=W)
        hatt = Label(detail,image=hat_icon, background='#fac031',anchor=W)
        time_txt2 = Label(detail,background='#fac031',foreground='black',width=6, text=diff,font='Times 10',anchor=W)
        favv = Label(detail,image=fav_icon, background='#fac031',anchor=W)
        matched = Label(detail,background='#fac031',foreground='black',text='null',font='Times 10',anchor=W)
        recipe_frame.grid(row=row, column=col, padx=40, pady=40)
        detail.grid()
        timer.grid(row=1,column=0)
        time_txt.grid(row=1,column=1,padx=1)
        hatt.grid(row=1,column=2)
        time_txt2.grid(row=1,column=3,padx=1)
        favv.grid(row=1,column=4,padx=1)
        matched.grid(row=1,column=5,padx=1)
        title.grid(row=2,pady=2)
        col = col+1
        if col == 3:
            col = 0
            row = row+1
        r = r+1
    root.update()
        
    canvas.configure(scrollregion=(0,0,fmz.winfo_width(),fmz.winfo_height()))

active_home_button()


def check_ingredients(recipe,ingri,id):
    count = int(0)
    for x in ingri:
            for z in recipe:
                if x in z:
                    count = count+1

    return count,id

# Search Function
def search():
    global canvas,fmz,recipe_frame,fav_icon,favs_icon,hat_icon,timer_icon
    dis_home()
    active_search_button()
    ingri = ingridients.get().replace(',',"")
    ingri.lower()
    ingri.split()
    ingri = ingri.split()
    print(ingri)

    for widget in canvas.winfo_children():
        widget.destroy()
        
    total_recipe = []
    cursor.execute("SELECT * FROM recipe;")
    for record in cursor.fetchall():
                id = record[0]
                recp = str(record[2])
                recp = recp.lower()
                recp = recp.split()
                info = check_ingredients(recp,ingri,id)
                count= info[0]  
                if count>1:
                    total_recipe.append(info[1])
    
    print(total_recipe)
    
    Time = Image.open("assets/timer.png")
    tim_rsz = Time.resize((20,20),Image.ANTIALIAS)
    timer_icon = ImageTk.PhotoImage(tim_rsz)

    #hat image 
    hat = Image.open("assets/hat.jpg")
    hat_rsz = hat.resize((20,20),Image.ANTIALIAS)
    hat_icon = ImageTk.PhotoImage(hat_rsz)

    #matched image
    fav = Image.open("assets/right.png")
    fav_rsz = fav.resize((25,25),Image.ANTIALIAS)
    fav_icon = ImageTk.PhotoImage(fav_rsz)

    #fav image
    favs = Image.open("assets/fav.png")
    favs_rsz = favs.resize((18,18),Image.ANTIALIAS)
    favs_icon = ImageTk.PhotoImage(favs_rsz)

    fmz = Frame(canvas,background='#28292e')
    canvas.create_window((0,0), window=fmz, anchor=NW)
    
    row = 0 
    col = 0
    x = 0
    
    for i in total_recipe:
        cursor.execute('select * from  public.recipe where "Recipe_id" = %s;',(i,))
        for record in cursor.fetchall():
            id = record[0]
            title_txt = record[1]
            recp = str(record[2])
            recp = recp.lower()
            recp = recp.split()
            time = record[4]
            diff = record[5]

        info = check_ingredients(recp,ingri,id)
        recipe_frame = LabelFrame(fmz, background='#fac031',width=250, height=200,bd=0,labelanchor=W)
        # importing Image
        my_image = Image.open("assets/"+title_txt+".jpg")
        # Resize image
        resized_image = my_image.resize((210,180),Image.ANTIALIAS)
        my_icon = ImageTk.PhotoImage(resized_image)

        myLabel = tk.Button(recipe_frame,bd=0,relief='solid',command=lambda k=i :get_recipe(k))
        myLabel.grid(column=0,row=0)
        myLabel.image = my_icon
        myLabel['image'] = my_icon
        detail = LabelFrame(recipe_frame, background='#fac031',bd=0)
        title = Label(recipe_frame, text=title_txt ,anchor=W,background='#fac031', font='Times 11',foreground='black',bd=0,height=2,width=24)
        timer = Label(detail,image=timer_icon, background='#fac031',anchor=W)
        time_txt = Label(detail,background='#fac031',foreground='black',width=6,text=time,font='Times 10',anchor=W)
        hatt = Label(detail,image=hat_icon, background='#fac031',anchor=W)
        time_txt2 = Label(detail,background='#fac031',foreground='black',width=6, text=diff,font='Times 10',anchor=W)
        favv = Label(detail,image=fav_icon, background='#fac031',anchor=W)
        matched = Label(detail,background='#fac031',foreground='black',text=info[0],font='Times 10',anchor=W)
        recipe_frame.grid(row=row, column=col, padx=40, pady=40)
        detail.grid()
        timer.grid(row=1,column=0)
        time_txt.grid(row=1,column=1,padx=1)
        hatt.grid(row=1,column=2)
        time_txt2.grid(row=1,column=3,padx=1)
        favv.grid(row=1,column=4,padx=1)
        matched.grid(row=1,column=5,padx=1)
        title.grid(row=2,pady=2)
        col = col+1
        if col == 3:
            col = 0
            row = row+1


    root.update()
    canvas.configure(scrollregion=(0,0,fmz.winfo_width(),fmz.winfo_height()))



dis_search()

root.geometry("900x800")
#root.resizable(False,False)
root.mainloop()




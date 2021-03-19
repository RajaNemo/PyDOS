from tkinter import *
import tkinter as tk

current_x, current_y = 0,0
color = "black"

def locate_xy(event):
    global current_x, current_y
    current_x, current_y = event.x, event.y
    
def addLine(event):
    global current_x, current_y
    canvas.create_line((current_x,current_y,event.x,event.y), fill = color)
    current_x, current_y = event.x, event.y

def show_color(new_color):
    global color 
    color = new_color


  

window = tk.Tk()
window.title("Van Gogh")
window.configure(bg='white')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

canvas = Canvas(window, bg="white")
canvas.grid(row=0, column=0, sticky='nsew')

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>',addLine)

id = canvas.create_rectangle((10,10,30,30), fill='black')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('black'))

id = canvas.create_rectangle((10,40,30,60), fill='gray')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('gray'))

id = canvas.create_rectangle((10,70,30,90), fill='Sienna')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('Sienna'))

id = canvas.create_rectangle((10,100,30,120), fill='red')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('red'))

id = canvas.create_rectangle((10,130,30,150), fill='coral')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('coral'))

id = canvas.create_rectangle((10,160,30,180), fill='gold')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('gold'))

id = canvas.create_rectangle((10,190,30,210), fill='green')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('green'))

id = canvas.create_rectangle((10,220,30,240), fill='DodgerBlue')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('DodgerBlue'))

id = canvas.create_rectangle((10,250,30,270), fill='pink2')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('pink2'))

id = canvas.create_rectangle((10,280,30,300), fill='white')
canvas.tag_bind(id, '<Button-1>', lambda x:show_color('white'))
#canvas.create_line(20,20,80,60)





window.mainloop()

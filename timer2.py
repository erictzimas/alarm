from tkinter import *

import time
import os
from time import strftime 
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
global c
c = -1
global count
global solve
count = 0
counti = 0
def clicked():
    global count
    global secs
    count += 1
    secs=int(hms_to_seconds(te.get()))
    global cii
    cii = int(hms_to_seconds(te.get())) 
    lbl2.pack()
    time2()
def clicked2():
    global solve
    time()
    lbl.pack(anchor = 'center')
def time():
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    
    lbl.after(1000, time)

def time2():
    global cii
    global solve
    k=0
    
    lbl2.config(text = convert(cii))
    cii = cii - 1
    if cii==-1:
        popupmsg("Time is up!")
    

    solve = lbl2.after(1000,time2)
    
    
def stop():
    global solve
    if solve:
        lbl2.after_cancel(solve)
       
     
   
     
    
    

def popupmsg(msg):
    global c
    popup = Tk()
    popup.resizable(False,False)
    popup.geometry("200x100")
    popup.wm_title("Alarm")
    label = Label(popup, text=msg, font=(NORM_FONT, 30))
    label.config(width=25)
    os.system('say "Time is up"')
    c = 0

    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.config(width=10)
    label.pack()

    B1.pack()
    popup.mainloop()       
        
def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)        
def hms_to_seconds(t):
    h, m, s = [int(i) for i in t.split(':')]
    return 3600*h + 60*m + s        

root = Tk()
root.title('Alarm')
w = Frame(root)

w.pack()


root.geometry("400x300")
lbl = Label(w,font = ('calibri', 40, 'bold'), 
            background = 'white', 
            foreground = 'black')
lbl.config(background='snow',fg='grey')
lbl2 = Label(w,font = ('calibri', 40, 'bold'), 
            background = 'white', 
            foreground = 'red')  
button = Button(w,command = clicked,text = "Start")
button.config(width = 20)
button2 = Button(w,command = clicked2,text = "Clock")
button2.config(width = 20)
button3 = Button(w, command = stop ,text = 'Stop')
button3.config(width=20)

te = Entry(w,text = "time in minutes")

te.config(background='snow')

lab = Label(w,text = 'Enter time in seconds')
lab.config(background='snow')

lab.pack()
te.pack()

button2.pack()
button.pack()
button3.pack()
root.resizable(False,False)

mainloop()

from tkinter import *
from tkinter.ttk import *
import time
import os
from time import strftime 
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
global c
c = -1
global togg 
togg = FALSE





def clicked():
    
   
   
    global secs
    secs=int(te.get())
    global cii
    cii = int(te.get())
    

    
    lbl2.pack()
    time2()
def clicked2():

    time()
    lbl.pack(anchor = 'center')
    
 


def time():
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time)
    

def time2():
    global cii
    
    lbl2.config(text = convert(cii))
    cii = cii - 1
    if cii==-1:
        popupmsg("Done")
    lbl2.after(1000,time2)
    











    togg = True
def popupmsg(msg):
    global c
    popup = Tk()
    popup.geometry("200x100")
    popup.wm_title("Alarm")
    label = Label(popup, text=msg, font=NORM_FONT)
    os.system('say "Time is up"')
    c = 0

    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack(anchor = 'center')
    popup.mainloop()       
        
def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)        
        

root = Tk()
root.title('Alarm')


root.geometry("400x200")
lbl = Label( root,font = ('calibri', 40, 'bold'), 
            background = 'white', 
            foreground = 'black')
lbl.config(background='snow')
lbl2 = Label( root,font = ('calibri', 40, 'bold'), 
            background = 'white', 
            foreground = 'black')  
button = Button(command = clicked,text = "Start")
button2 = Button(command = clicked2,text = "Clock")

te = Entry(text = "time in minutes")


te.config(background='snow')


lab = Label(text = 'Enter time in seconds')
lab.config(background='snow')

lab.pack()
te.pack()


button2.pack()
button.pack()


mainloop()

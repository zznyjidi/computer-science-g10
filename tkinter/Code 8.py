from tk_scene import scene
from tkinter import *

sceneLayout = (
    (())
)

w = Tk()

def day():
    global Sun
    global Moon
    Sun = True
    Moon = False
    return True

instruction = Label(w, text='''Welcome User428, this is the CIA's secret"\
    operation. Operation SKYFALL.
    During 1898, we have replaced birds with drones,"\
    and now in the past 5 years we have"\
    been working on deleting the sky ")
    Lets see how loyal you are to our cause…''')

l1 = Label(w, text="Is it Day or Night"\
                         "real? (Enter \"day\" or \"night\")")
buttonDay = Button(w, text='Day', command=day)

w.mainloop()

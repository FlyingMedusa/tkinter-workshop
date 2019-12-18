import tkinter
from tkinter.messagebox import *

top = tkinter.Tk()

def print_text(ent):
    tkinter.messagebox.showinfo('Info', ent.get())

entry1 = tkinter.Entry(top, width=50)
entry1.pack(side='left')

button_print = tkinter.Button(top, text='Print text', command=lambda: print_text(entry1))
button_print.pack(side='left')

top.mainloop()

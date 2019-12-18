import tkinter
from tkinter.filedialog import *

top = tkinter.Tk()

def print_file():
    f = tkinter.filedialog.askopenfilename(
        parent=top, initialdir='/',
        title='Chose file',
        filetypes=[('markdown files','.md')]
    )
    fc = open(f, 'r')
    print(fc.read())

b1 = tkinter.Button(top, text='Print file content', command=print_file)
b1.pack(anchor='w')

top.mainloop()

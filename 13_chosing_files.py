import tkinter
from tkinter.filedialog import *

top = tkinter.Tk()

def display_image():
    f = tkinter.filedialog.askopenfilename(
        parent=top, initialdir='/',
        title='Chose file',
        filetypes=[('png images','.png'),
                   ('gif images', '.gif')]
    )
    new_window = tkinter.Toplevel(top)

    image = tkinter.PhotoImage(file=f)
    l1 = tkinter.Label(new_window, image=image)
    l1.image = image
    l1.pack()

b1 = tkinter.Button(top, text='Display image', command=display_image)
b1.pack(fill='x')

top.mainloop()

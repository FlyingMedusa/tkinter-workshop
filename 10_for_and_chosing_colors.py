import tkinter

top = tkinter.Tk()

colors = [
    ('Red', 'red'),
    ('Green', 'green'),
    ('Blue', 'blue'),
    ('White', 'white')
]

v = tkinter.StringVar()
v.set('red')  # the default setting

for text, color in colors:
    b = tkinter.Radiobutton(top, text=text, variable=v, value=color)
    b.pack(anchor='w')


def color_me():
    b1.configure(bg=v.get())


b1 = tkinter.Button(top, text='COLOR ME!', command=color_me)
b1.pack(anchor='w', fill='x')

top.mainloop()
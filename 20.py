import tkinter

top = tkinter.Tk()

top.wm_title('Hello...')

top.resizable(width='false', height='false')
top.minsize(width=230, height=100)
top.minsize(width=230, height=100)

label1 = tkinter.Label(top, text='...world!')
label1.pack()

b_close = tkinter.Button(top, text='Close', command=top.destroy)
b_close.pack(fill='x')

top.mainloop()
import tkinter

top = tkinter.Tk()

top.wm_title('Hello...')

frame1 = tkinter.Frame(top, borderwidth=2, relief='ridge')
frame1.grid(row=0, column=0, sticky='ns')
frame2 = tkinter.Frame(top, borderwidth=2, relief='raised')
frame2.grid(row=0, column=1, sticky='ns')
frame3 = tkinter.Frame(top, borderwidth=2, relief='ridge')
frame3.grid(row=1, column=0, sticky='ew')

label1 = tkinter.Label(frame1, text='...world!')
label1.pack()

b_close = tkinter.Button(frame2, text='Close', command=top.destroy, fg='white', bg='red')
b_close.pack(fill='x')

b_color = tkinter.Button(frame3, text='Color')
b_color.pack()

top.mainloop()
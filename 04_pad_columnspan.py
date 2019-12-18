import tkinter

top = tkinter.Tk()

top.wm_title('Hello...')

frame1 = tkinter.Frame(top, borderwidth=2, relief='ridge', pady=4, padx=4)
frame1.grid(row=0, column=0, sticky='ns')
frame2 = tkinter.Frame(top, borderwidth=2, relief='raised', pady=4, padx=4)
frame2.grid(row=0, column=1, sticky='ns')
frame3 = tkinter.Frame(top, borderwidth=2, relief='ridge', pady=4, padx=4)
frame3.grid(row=1, column=0, sticky='ew', columnspan=2)

label1 = tkinter.Label(frame1, text='Hello world!', fg='darkcyan')
label1.pack()

b_close = tkinter.Button(frame2, text='Close', command=top.destroy, fg='white', bg='red')
b_close.pack()

b_color = tkinter.Button(frame3, text='Color')
b_color.pack(fill='x')

top.mainloop()
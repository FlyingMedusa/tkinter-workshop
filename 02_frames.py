import tkinter

top = tkinter.Tk()

top.wm_title('Hello...')

frame1 = tkinter.Frame(top, borderwidth=2, relief='sunken')
#relief: flat, raised, sunken, groove, ridge
frame2 = tkinter.Frame(top, borderwidth=2, relief='ridge')
frame1.pack(fill='y', side='left')
frame2.pack(fill='y', side='left')

label1 = tkinter.Label(frame1, text='...world!')
label1.pack()

b_close = tkinter.Button(frame2, text='Close', command=top.destroy)
b_close.pack(fill='x')

top.mainloop()
import tkinter

top = tkinter.Tk()

top.minsize(width=300, height=300)
top.minsize(width=300, height=300)

button2 = tkinter.Button(top, text="BUTTON", relief='ridge', fg='white', bg='darkcyan')
button2.pack()
#place and pack can coexist (not like grid and pack)

button1 = tkinter.Button(top, text='B')
button1.place(relx=0.5, rely=0.0, anchor="center")
#center can be replaced by: 'n', 's', 'e', 'w', 'ne' ... itd.

top.mainloop()
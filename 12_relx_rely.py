import tkinter

top = tkinter.Tk()

top.configure(background='darkcyan')
top.minsize(width=300, height=300)
top.minsize(width=300, height=300)

button2 = tkinter.Button(top, text="BUTTON", relief='ridge', fg='darkred', bg='pink')
button2.pack(fill='x')
#place and pack can coexist (not like grid and pack)

button1 = tkinter.Button(top, text='Another Button', relief='ridge', pady=4, padx=4)
button1.place(relx=0.5, rely=0.5, anchor="center")
#center can be replaced by: 'n', 's', 'e', 'w', 'ne' ... itd.

top.mainloop()
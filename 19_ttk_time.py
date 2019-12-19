import tkinter
import time
from tkinter import ttk

top = tkinter.Tk()

def start():
    for k in range(1, 11):
        progress_var.set(k)
        print("STEP",k)
        time.sleep(0.3)
        top.update_idletasks()

b1 = tkinter.Button(top, text="START", command=start)
b1.pack(side="left")

progress_var = tkinter.DoubleVar()

pb = ttk.Progressbar(top, orient="horizontal",
                     length=200, maximum=10,
                     mode="determinate",
                     var=progress_var)

pb.pack(side="left")
pb["value"] = 0

top.mainloop()
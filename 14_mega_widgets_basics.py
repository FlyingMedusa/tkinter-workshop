import tkinter
import Pmw

top = tkinter.Tk()

entry_firstname = Pmw.EntryField(top, labelpos="w",
                                 label_text="First name: ",
                                 entry_bg="white",
                                 entry_width=25,
                                 validate="alphabetic")
entry_firstname.pack(anchor='e')

top.mainloop()
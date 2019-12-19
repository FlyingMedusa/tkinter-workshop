import tkinter
import Pmw

top = tkinter.Tk()

entry_firstname = Pmw.EntryField(top, labelpos="w",
                                 label_text="First name: ",
                                 entry_bg="white",
                                 entry_width=25,
                                 validate="alphabetic")
entry_lastname = Pmw.EntryField(top, labelpos="w",
                                 label_text="Last name: ",
                                 entry_bg="white",
                                 entry_width=25,
                                 validate="alphabetic")
entry_birth = Pmw.EntryField(top, labelpos="w",
                                 label_text="Date of birth: ",
                                 entry_bg="white",
                                 entry_width=25,
                                 validate="date")
entry_weight = Pmw.EntryField(top, labelpos="w",
                                 label_text="Weight [kg]: ",
                                 entry_bg="white",
                                 entry_width=25,
                                 validate={"validator": "integer",
                                           "min": 1, "max": 24}) #value from 1 to 24
entry_firstname.pack(anchor='e')
entry_lastname.pack(anchor='e')
entry_birth.pack(anchor='e')
entry_weight.pack(anchor='e')

top.mainloop()
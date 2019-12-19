import tkinter
import Pmw

top = tkinter.Tk()

notebook = Pmw.NoteBook(top)
notebook.pack(fill="both", padx=10, pady=10)

page1 = notebook.add("Page 1")
page2 = notebook.add("Page 2")
page3 = notebook.add("Page 3")
page4 = notebook.add("Page 4")

tkinter.Label(page1, text="This is page 1").pack()
tkinter.Label(page2, text="This is page 2").pack()
tkinter.Label(page3, text="This is page 3").pack()
tkinter.Label(page4, text="This is page 4").pack()

notebook.tab("Page 1").focus_set()

top.mainloop()

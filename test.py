from Tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.focus_set()

def callback():
    print e.get()

b = Button(root, text="get", width=10, command=callback).pack()
mainloop()

e = Entry(root, width=50).pack()
content.set(content.get())

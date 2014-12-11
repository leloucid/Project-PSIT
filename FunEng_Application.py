'''FunEng Application'''
from Tkinter import *
root = Tk()

#Head
one = Label(root, text="Fun English A bit Everyday!"\
            , font=("Helvetica", 35), fg="#5f62d9").grid(row=0 ,column=1)
#Photo for app
avatar = PhotoImage(file="avatar.gif")
bubble = PhotoImage(file="bubble.gif")
pic_1 = Label(root, image=avatar).grid(row=2, column=0)
pic_2 = Label(root, image=bubble).grid(row=2, column=1)

#Box to type + sent button
Answer = Entry(root).grid(row=3, column=1)
sent = Button(root, text="Sent!", font=("Helvetica", 14)\
              , fg="#5f62d9", bg="#e8f5ff", command=root.destroy)
sent.grid(row=4, column=1)

#Quit button
qui = Button(root, text="Quit", font=("Helvetica", 14)\
              , fg="#5f62d9", bg="#e8f5ff", command=root.destroy)
qui.grid(row=4, column=2)

#Answer box 
answer = Message(root, text="Hey! Do you want to know meaning of which word?"\
                 , font=("Helvetica", 15)\
               , fg="#5f62d9", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)

root.mainloop()

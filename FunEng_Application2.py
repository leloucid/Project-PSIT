'''FunEng Application'''
from Tkinter import *
import random
root = Tk()
#Head


dct = {'cat':'Animal that have two triangle ear', \
       'dog':'That sound box box',\
       'cafeeyen':'cat of IT ladkrabang', \
       'poji':'a very bad slime'}
wrd = random.choice(dct.values())

one = Label(root, text="Fun English A bit Everyday!"\
            , font=("Helvetica", 35), fg="#5f62d9").grid(row=0 ,column=1)
#Photo for app
avatar = PhotoImage(file="avatar.gif")
bubble = PhotoImage(file="bubble.gif")
pic_1 = Label(root, image=avatar).grid(row=2, column=0)
pic_2 = Label(root, image=bubble).grid(row=2, column=1)

def printcheck():
    print type(answer)
    if answer.lower() in dct.keys():
        print 'Correct'
    else:
        print 'kakkkkkkkkkkkkkkk'
    

#Box to type + sent button
answer = Entry(root).grid(row=3, column=1)
sent = Button(root, text="Sent!", font=("Helvetica", 14)\
              , fg="#5f62d9", bg="#e8f5ff", command=printcheck)
sent.grid(row=4, column=1)

#Answer box 
answer = Message(root, text="%s" % (wrd)\
                 , font=("Helvetica", 15)\
               , fg="#5f62d9", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)

#Quit button
qui = Button(root, text="Quit", font=("Helvetica", 14)\
              , fg="#5f62d9", bg="#e8f5ff", command=root.destroy)
qui.grid(row=4, column=2)

root.mainloop()

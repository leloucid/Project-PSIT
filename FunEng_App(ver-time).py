# -*- coding: UTF-8 -*-
'''FunEng Application'''
from Tkinter import *
import random
root = Tk()



#Head


dct = {'cat':'Animal that have two triangle ear', \
       'dog':'That sound box box',\
       'cafeeyen':'cat of IT ladkrabang', \
       'poji':'a very bad slime', \
       'jong':'จงจงจงทดสอบไทย'}
wrd = random.choice(dct.values())

one = Label(root, text="Fun English A bit Everyday!"\
            , font=("Helvetica", 35), fg="#5f62d9").grid(row=0 ,column=1)
#Photo for app
avatar = PhotoImage(file="avatar.gif")
bubble = PhotoImage(file="bubble.gif")
pic_1 = Label(root, image=avatar).grid(row=2, column=0)
pic_2 = Label(root, image=bubble).grid(row=2, column=1)

def printcheck(answer):
    print type(answer)
    if answer.lower() in dct.keys():
        print 'Correct'
        wrd = random.choice(dct.values())
        answer_2 = Message(root, text="%s" % (wrd)\
                 , font=("Helvetica", 19)\
               , fg="#5f62d9", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)
    else:
        print 'Not Correct'

#timer
import Tkinter as tk
import time

def start():
    global count_flag
    count_flag = True
    count = 0.0
    while True:
        if count_flag == False:
            break
        # put the count value into the label
        label['text'] = str(count)
        # wait for 0.1 seconds
        time.sleep(0.1)
        # needed with time.sleep()
        root.update()
        # increase count
        count += 0.1
def stop():
    global count_flag
    count_flag = False
# this will be a global flag
count_flag = True
# create needed widgets
label = tk.Label(root, text='0.0')
btn_start = tk.Button(root, text='start', command=start)
btn_stop = tk.Button(root, text='stop', command=stop)
# use a grid to place the widgets
label.grid(row=0, column=0, columnspan=2)
btn_start.grid(row=1, column=0, padx=5, pady=5)
btn_stop.grid(row=1, column=1, padx=5)


#Quit button
qui = Button(root, text="Quit", font=("Helvetica", 14)\
              , fg="#5f62d9", bg="#e8f5ff", command=root.destroy)
qui.grid(row=4, column=2)

#Answer box 
answer_2 = Message(root, text="%s" % (wrd)\
                 , font=("Helvetica", 15)\
               , fg="#5f62d9", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)


mainloop()

# -*- coding: UTF-8 -*-
'''FunEng Application'''
from Tkinter import *
import random
import winsound

class MainApp:
    #constructor
    def __init__(self,mainwindow):
        mainwindow.title("FunEng Application")
    
#create a Tk root widget, a simple window
root = Tk()
#create an object from class App
app = MainApp(root)

#Head
'''
English practice game more and more fun!
'''
point = 0
dct = {'expect':'คาดหวัง', \
       'energetic':'กระปรี้กระเปร่า',\
       'effect':'ผลกระทบ', \
       'irony':'การถากถาง', \
       'kinetic':'เกี่ยวกับการเคลื่อนไหว',\
       'nanotechnology':'นาโนเทคโนโลยี',\
       'nervous':'ประหม่า',\
       'plasma':'ส่วนที่เป็นนํ้าสีเหลืองในเลือด',\
       'reparation':'การซ่อมแซม',\
       'respiration':'การหายใจ',\
       'taxonomy':'การจัดแบ่งสิ่งมีชีวิต',\
       'vortex':'กระแสนํ้าที่หมุนวน',\
       'signature':'ลงลายมือชื่อ',\
       'terminal':'สถานี',\
       'crew':'ลูกเรือ',\
       'customs':'ศุลกากร',\
       'florist':'ร้านขายดอกไม้',\
       'patient':'อดทน',\
       'mental':'เกี่ยวกับจิตใจ',\
       'acceptable':'ยอมรับได้',\
       'nonsense':'เรื่องไร้สาระ',\
       'obedience':'การเชื่อฟังคำสั่ง',\
       'photography':'การถ่ายภาพ',\
       'possibility':'ความเป็นไปได้',\
       'quantity':'ปริมาณ',\
       'quality':'คุณภาพ',\
       'refuse':'ปฏิเสธ',\
       'religion':'ศาสนา',\
       'satisfy':'ทำให้พอใจ',\
       'secretary':'เลขานุการ',\
       'shelter':'ที่หลบภัย',\
       'shopkeeper':'เจ้าของร้าน',\
       'similar':'ที่คล้ายกัน',\
       'transparent':'โปร่งใส',\
       'urgent':'ด่วน',\
       'wages':'ค่าจ้าง',\
       'wander':'ร่อนเร่',\
       'librarian':'บรรณารักษ์',\
       'landlord':'เจ้าของที่ดิน',\
       'memorial':'อนุสรณ์',\
       'advertise':'โฆษณา',\
       'against':'ต่อต้าน',\
       'century':'ศตวรรษ',\
       'civilization':'อารยธรรม',\
       'demand':'ความต้องการ',\
       'existence':'การดำรงอยู่',\
       'government':'รัฐบาล',\
       'guidance':'คำแนะนำ',\
       'honor':'เกียรติ',\
       'infection':'การติดเชื้อ',\
       'marriage':'การแต่งงาน',\
       'military':'ทหาร',\
       'nerve':'เส้นประสาท',\
       'parliament':'รัฐสภา',\
       'tribe':'เผ่า'}
wrd = random.choice(dct.values())
#Photo for app
avatar = PhotoImage(file="Poji3.gif")
bubble = PhotoImage(file="bubble2.gif")
wrong  = PhotoImage(file="Poji2.gif")
right  = PhotoImage(file="Poji.gif")
top = PhotoImage(file="top1.gif")
gm = PhotoImage(file="gm.gif")
pic_1 = Label(root, image=avatar).grid(row=2, column=0)
pic_2 = Label(root, image=bubble).grid(row=2, column=1)
header = Label(root, image=top).grid(row=0, column=1)
gamemaster = Label(root, image=gm).grid(row=0, column=0)
def printcheck(answer, point):
    '''
    check if the answer is right or wrong
    '''
    print type(answer)
    global wrd
    if dct.has_key(answer.lower()) == True and dct[answer.lower()] == wrd :
        answer_2 = Message(root, text="                                    "\
                    , font=("Helvetica", 19)\
                , fg="#9a2f2f", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)
        wrd = random.choice(dct.values())
        answer_2 = Message(root, text="%s" % (wrd)\
                    , font=("Helvetica", 19)\
                , fg="#9a2f2f", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)
        pic_3 = Label(root, image=right).grid(row=2, column=0)
        winsound.PlaySound('b.wav',winsound.SND_FILENAME)
        print 'Correct'
    else:
        pic_4 = Label(root, image=wrong).grid(row=2, column=0)
        winsound.PlaySound('a.wav',winsound.SND_FILENAME)
        print 'Not Correct'

#Box to type + sent button
point = Entry(root)        
answer = Entry(root)
answer.grid(row=4, column=1)
sent = Button(root, text="Sent!", font=("Helvetica", 14)\
              , fg="#ff4e4e", bg="#e8f5ff", command= lambda: printcheck(answer.get(), point))
sent.grid(row=5, column=1)
point = 0

#Quit button
qui = Button(root, text="Quit", font=("Helvetica", 14)\
              , fg="#ff4e4e", bg="#e8f5ff", command=root.destroy)
qui.grid(row=5, column=2)

#Answer box 
answer_2 = Message(root, text="%s" % (wrd)\
                 , font=("Helvetica", 19)\
               , fg="#9a2f2f", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)

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
label = tk.Label(root, text='0.0', font = ("Helvetica", 20), fg="#ff9584")
btn_start = tk.Button(root, text='start', command=start, \
                      font=("Helvetica", 10), fg="#9a2f2f", bg="#e8f5ff")
btn_stop = tk.Button(root, text='stop', command=stop, \
                     font=("Helvetica", 10), fg="#9a2f2f", bg="#e8f5ff")
# use a grid to place the widgets
label.grid(row=3, column=0, columnspan=1)
# start 
btn_start.grid(row=4, column=0, padx=1, pady=1)
# stop
btn_stop.grid(row=5, column=0, padx=1)

mainloop()

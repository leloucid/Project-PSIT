# -*- coding: UTF-8 -*-
'''FunEng Application'''
from Tkinter import *
import random
import winsound
root = Tk()
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
       'taxonomy':'การจัดแบ่งสิ่งมีชีวิตออกเป็นกลุ่มต่างๆ',\
       'vortex':'กระแสลม หรือกระแสนํ้าที่หมุนวน ',\
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
       'memorial':'อนุสรณ์'}
wrd = random.choice(dct.values())
one = Label(root, text="Fun English A bit Everyday!"\
            , font=("Helvetica", 35), fg="#5f62d9").grid(row=0 ,column=1)
#Photo for app
avatar = PhotoImage(file="Poji3.gif")
bubble = PhotoImage(file="bubble2.gif")
wrong  = PhotoImage(file="Poji2.gif")
right  = PhotoImage(file="Poji.gif")
pic_1 = Label(root, image=avatar).grid(row=2, column=0)
pic_2 = Label(root, image=bubble).grid(row=2, column=1)


def printcheck(answer, point):
    print type(answer)
    global wrd
    if dct.has_key(answer.lower()) == True:
        print 'yes'
    if answer.lower() in dct.keys():
        answer_2 = Message(root, text="                         "\
                    , font=("Helvetica", 19)\
                , fg="#2a3373", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)
        wrd = random.choice(dct.values())
        answer_2 = Message(root, text="%s" % (wrd)\
                    , font=("Helvetica", 19)\
                , fg="#2a3373", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)
        pic_3 = Label(root, image=right).grid(row=2, column=0)
        winsound.PlaySound('b.wav',winsound.SND_FILENAME)
    else:
        pic_4 = Label(root, image=wrong).grid(row=2, column=0)
        winsound.PlaySound('a.wav',winsound.SND_FILENAME)

#Box to type + sent button
point = Entry(root)        
answer = Entry(root)
answer.grid(row=3, column=1)
sent = Button(root, text="Sent!", font=("Helvetica", 14)\
              , fg="#5f62d9", bg="#e8f5ff", command= lambda: printcheck(answer.get(), point))
sent.grid(row=4, column=1)
point = 0
#Answer box 
answer_2 = Message(root, text="%s" % (wrd)\
                 , font=("Helvetica", 15)\
               , fg="#2a3373", width=200, justify=LEFT, anchor=N).grid(row=2 ,column=1)

mainloop()

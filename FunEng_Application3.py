# -*- coding: UTF-8 -*-
'''FunEng Application'''
from Tkinter import *
import random
import winsound
import time

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
       'plasma':'ส่วนที่เป็นนํ้าสีเหลือง',\
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
       'tribe':'เผ่า',\
       'substance':'เนื้อหา,ใจความ',\
       'especially':'โดยเฉพาะ',\
       'perhaps':'บางที',\
       'pharmacist':'เภสัชกร',\
       'inspector':'สารวัตร',\
       'tempestuous':'ซึ่งมีพายุแรง',\
       'subjugate':'ปราบปราม',\
       'supercilious':'ดูถูก,เหยียดหยาม',\
       'nihilism':'การก่อการร้าย',\
       'notarize':'รับรอง,จดทะเบียน',\
       'parameter':'ตัวแปร',\
       'quality':'คุณภาพ',\
       'manufacture':'โรงงาน',\
       'scheme':'แบบแผน',\
       'partition':'การแบ่งแยก',\
       'paramount':'ซึ่งมีอำนาจสูงสุด',\
       'pamphlet':'แผ่นพับ',\
       'abundance':'อุดมสมบูรณ์',\
       'abstract':'ที่เป็นนามธรรม',\
       'barrister':'เนติบัณฑิต',\
       'barricade':'สิ่งกีดขวาง',\
       'candidate':'ผู้สมัครรับเลือกตั้ง',\
       'cabinet':'คณะรัฐมนตรี',\
       'obvious':'ชัดเจน,เด่นชัด',\
       'obscure':'คลุมเครือ,มืดมัว',\
       'reason':'เหตุผล',\
       'rarely':'อย่างหายาก',\
       'rapidly':'อย่างรวดเร็ว',\
       'rebate':'ส่วนลด,เงินคืน',\
       'rebuke':'ต่อว่า,ตำหนิ',\
       'headquarters':'สำนักงานใหญ่',\
       'haughty':'โอหัง,ถือตัว',\
       'warehouse':'โกดังสินค้า',\
       'nevertheless':'อย่างไรก็ตาม',\
       'neighborhood':'บ้านใกล้เรือนเคียง',\
       }
wrd = random.choice(dct.values())


#Photo for app
avatar = PhotoImage(file="Poji3.gif")
bubble = PhotoImage(file="bubble2.gif")
wrong  = PhotoImage(file="Poji2.gif")
right  = PhotoImage(file="Poji.gif")
top = PhotoImage(file="top1.gif")
gm = PhotoImage(file="gm.gif")
time_1 = PhotoImage(file="time.gif")
score_1 = PhotoImage(file="score.gif")
answer_1 = PhotoImage(file="answer.gif")
desk = PhotoImage(file="desk.gif")
notice = PhotoImage(file="notice.gif")
pic_1 = Label(root, image=avatar).grid(row=2, column=0, sticky=S)
pic_2 = Label(root, image=bubble).grid(row=2, column=1)
notice_1 = Label(root, image=notice).grid(row=0, column=2)
header = Label(root, image=top).grid(row=0, column=1)
gamemaster = Label(root, image=gm).grid(row=0, column=0)
score_word = Label(root, image=score_1).grid(row=3, column=2)
time_word = Label(root, image=time_1).grid(row=3, column=0)
answer_word = Label(root, image=answer_1).grid(row=3, column=1)
desk_1 = Label(root, image=desk).grid(row=2, column=2, sticky=S)
score = 0
score_board = Message(root, text=score\
                    , font=("Helvetica", 19)\
                , fg="#9a2f2f", anchor=S).grid(row=4 ,column=2)

def printcheck(answer, point):
    '''
    check if the answer is right or wrong
    '''
    print type(answer)
    global wrd
    global score
    if dct.has_key(answer.lower()) == True and dct[answer.lower()] == wrd :
        answer_2 = Message(root, text="                                    "\
                , font=("Helvetica", 19)\
                , fg="#9a2f2f", width=200, justify=LEFT,\
                anchor=N).grid(row=2 ,column=1)
        wrd = random.choice(dct.values())
        answer_2 = Message(root, text="%s" % (wrd)\
                , font=("Helvetica", 19)\
                , fg="#9a2f2f", width=200, justify=LEFT,\
                anchor=N).grid(row=2 ,column=1)
        pic_3 = Label(root, image=right).grid(row=2, column=0, sticky=S)
        winsound.PlaySound('b.wav',winsound.SND_FILENAME)
        print 'Correct'
        score += 10
        score_board = Message(root, text=score\
                , font=("Helvetica", 19)\
                , fg="#9a2f2f", anchor=S).grid(row=4 ,column=2)
        if score == 300:
            stop()
            endding = Message(root, text="<< GAME END! see your score"\
                    , font=("Helvetica", 19), width=500\
                , fg="#9a2f2f", anchor=S).grid(row=2 ,column=1)
    else:
        pic_4 = Label(root, image=wrong).grid(row=2, column=0, sticky=S)
        winsound.PlaySound('a.wav',winsound.SND_FILENAME)
        print 'Not Correct'

#Box to type + sent button
point = Entry(root)        
answer = Entry(root)
answer.grid(row=4, column=1)
sent = Button(root, text="Sent!", font=("Helvetica", 14)\
              , fg="#ff4e4e", bg="#e8f5ff",\
              command= lambda: printcheck(answer.get(), point))
sent.grid(row=5, column=1)
point = 0

#Answer box 
answer_2 = Message(root, text="%s" % (wrd)\
                 , font=("Helvetica", 19)\
               , fg="#9a2f2f", width=200, justify=LEFT,\
                anchor=N).grid(row=2 ,column=1)

#timer

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
def quiting():
    stop()
    root.destroy()
# this will be a global flag
count_flag = True
# create needed widgets
label = Label(root, text='0.0', font = ("Helvetica", 20), fg="#ff9584")
btn_start = Button(root, text='Start', command=start, \
                   font=("Helvetica", 14), fg="#9a2f2f", bg="#e8f5ff")
# use a grid to place the widgets
label.grid(row=4, column=0, columnspan=1)
# start 
btn_start.grid(row=5, column=0, padx=1, pady=1)

# Answer


#Quit button
qui = Button(root, text="Quit", font=("Helvetica", 14)\
              , fg="#ff4e4e", bg="#e8f5ff",\
             justify=RIGHT, command=quiting)
qui.grid(row=5, column=2, sticky=SE)


mainloop()

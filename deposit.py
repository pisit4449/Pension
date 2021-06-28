from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime


########## สร้าง GUI ################################

GUI = Tk()
GUI.title("Program ฝากเงินเบี้ยยังชีพ V.1.0")
w = 600
h = 650
ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2) - 50
GUI.geometry(f"{w}x{h}+{x:.0f}+{y:.0f}")

FONT1 = (None, 14)
FONT2 = (None, 10)

################# Menu Bar ##########################

menubar = Menu(GUI)
GUI.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
######## Menu File############
def runFile():
    messagebox.showinfo('RUN','Test Run')

def Exit():
    check = messagebox.askyesno('EXIT','คุณต้องการออกจากโปรแกรมใช่หรือไม่')
    if check == True:
        GUI.destroy()
    else:
        pass

menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Run', command=runFile)
filemenu.add_command(label='Exit', command=Exit)

######## Menu Help ###########

def About():
    messagebox.showinfo('About','Sinyapong Sukito')

def readMe():
    messagebox.showinfo('Help', 'กรูณาช่วยตัวเองไปก่อน')

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=About)
helpmenu.add_command(label='Read Me', command=readMe)

################# Tab ###############################

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

############## รูป Icon ###############
Icon_T1 = PhotoImage(file='Money_T1.png')
Icon_T2 = PhotoImage(file='Money_T2.png')
Icon_T3 = PhotoImage(file='Money_T3.png')
############## Tab ###################
Tab.add(T1, text=f'{"สูงอายุ": ^{25}}', image=Icon_T1, compound='top')
Tab.add(T2, text=f'{"พิการ": ^{25}}', image=Icon_T2, compound='top')
Tab.add(T3, text=f'{"เอดส์": ^{25}}', image=Icon_T3, compound='top')

############### Frame สูงอายุ ################################

F1 = Frame(T1)
F1.pack(pady=10)

########## ช่องใส่ข้อความ ##########
L = ttk.Label(F1, text='จำนวนเงินสูงอายุที่เหลือ', font=FONT1, foreground='green').pack(pady=5)
L60 = ttk.Label(F1, text='อายุ 60 ปี(คน)', font=FONT2).pack()
old_sixty = StringVar()
E1 = ttk.Entry(F1, textvariable=old_sixty, font=FONT2)
E1.pack()

L70 = ttk.Label(F1, text='อายุ 70 ปี(คน)', font=FONT2).pack()
old_seventy = StringVar()
E2 = ttk.Entry(F1, textvariable=old_seventy, font=FONT2)
E2.pack()

L80 = ttk.Label(F1, text='อายุ 80 ปี(คน)', font=FONT2).pack()
old_eiaghty = StringVar()
E3 = ttk.Entry(F1, textvariable=old_eiaghty, font=FONT2)
E3.pack()

L90 = ttk.Label(F1, text='อายุ 90 ปี(คน)', font=FONT2).pack()
old_ninety = StringVar()
E4 = ttk.Entry(F1, textvariable=old_ninety, font=FONT2)
E4.pack()

L = ttk.Label(F1, text='จำนวนเงินพิการที่เหลือ', font=FONT1, foreground='green').pack(pady=5)
L19 = ttk.Label(F1, text='อายุเกิน 18 ปี(คน)', font=FONT2).pack()
eightty = StringVar()
E5 = ttk.Entry(F1, textvariable=eightty, font=FONT2)
E5.pack()

L18 = ttk.Label(F1, text='อายุต่ำกว่า 18 ปี(คน)', font=FONT2).pack()
over = StringVar()
E6 = ttk.Entry(F1, textvariable=over, font=FONT2)
E6.pack()

L = ttk.Label(F1, text='จำนวนเงินเอดส์ที่เหลือ', font=FONT1, foreground='green').pack(pady=5)
La = ttk.Label(F1, text='เอดส์(คน)', font=FONT2).pack()
aids = StringVar()
E7 = ttk.Entry(F1, textvariable=aids, font=FONT2)
E7.pack()

saveicon = PhotoImage(file='save.png')
B2 = ttk.Button(F1, text='SAVE', image=saveicon, compound='left')
B2.pack(ipadx=5, ipady=5 , pady=10)

V_result = StringVar()
V_result.set('---------------------------')
result = ttk.Label(F1, textvariable=V_result, font=FONT1, foreground='green')
result.pack(pady=20)

GUI.mainloop()
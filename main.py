import tkinter as tk
from tkinter import *
import math
window=tk.Tk()
window.title('Basic Calculator')

def myclick(number):
    n=e.get()
    e.delete(0,tk.END)
    e.insert(0,str(n)+str(number))
    
def clr():
    e.delete(0,tk.END)
    
def add():
    n1=e.get()
    global f_num
    global operation
    operation='addition'
    f_num=int(n1)
    clr()
    
def mply():
    n1=e.get()
    global f_num
    global operation
    operation='multiplication'
    f_num=int(n1)
    clr()
    
def sub():
    n1=e.get()
    global f_num
    global operation
    operation='subtraction'
    f_num=int(n1)
    clr()
    
def div():
    n1=e.get()
    global f_num
    global operation
    operation='division'
    f_num=int(n1)
    clr()
    
def prcnt():
    n1=e.get()
    global f_num
    global operation
    operation='percentage'
    f_num=int(n1)
    clr()
    
def sqt():
    n1=e.get()
    global f_num
    global operation
    operation='squareroot'
    f_num=int(n1)
    clr()
    e.insert(0,math.sqrt(f_num))
    
def square():
    n1=e.get()
    global f_num
    global operation
    operation='square'
    f_num=int(n1)
    clr()
    
def sin():
    n1=e.get()
    global f_num
    global operation
    operation='sin'
    f_num=int(n1)
    clr()
    e.insert(0,math.sin(f_num))
    
def cos():
    n1=e.get()
    global f_num
    global operation
    operation='cos'
    f_num=int(n1)
    clr()
    e.insert(0,math.cos(f_num))
    
def tan():
    n1=e.get()
    global f_num
    global operation
    operation='tan'
    f_num=int(n1)
    clr()
    e.insert(0,math.tan(f_num))
    
def log():
    n1=e.get()
    global f_num
    global operation
    operation='log'
    f_num=int(n1)
    clr()
    try:
        e.insert(0,math.log(f_num))
    except:
         e.insert(0,'-infinity')
    
def equalto():
    n2=e.get()
    clr()
    if operation=='addition':
        e.insert(0,f_num+int(n2))
    elif operation=='subtraction':
        e.insert(0,f_num-int(n2))
    elif operation=='multiplication':
        e.insert(0,f_num*int(n2))
    elif operation=='division':
        try:
            e.insert(0,f_num/int(n2))
        except:
            e.insert(0,"can't divided by zero")
    elif operation=='percentage':
        e.insert(0,(f_num/int(n2)*100))
    elif operation=='square':
        e.insert(0,f_num**int(n2))
        
frame=LabelFrame(window,padx=5,pady=5,bd=10,bg='#EEEEE3')
frame.grid(padx=10,pady=10)
e=tk.Entry(frame,width=22,bg='#bdb76b',font=(50),border=7,justify='right')
e.grid(row=0,column=0,columnspan=4,pady=7)

b1=tk.Button(frame,text='1',padx=20,pady=15,command=lambda: myclick(1),bg='#ffebcd',border=4)
b1.grid(row=3,column=0)
b2=tk.Button(frame,text='2',padx=20,pady=15,command=lambda: myclick(2),bg='#ab4e52',border=4)
b2.grid(row=3,column=1)
b3=tk.Button(frame,text='3',padx=20,pady=15,command=lambda: myclick(3),bg='#ab4e52',border=4)
b3.grid(row=3,column=2)
b_mply=tk.Button(frame,text='*',padx=22,pady=15,command=mply,bg='#66cdaa',border=4)
b_mply.grid(row=3,column=3)

b4=tk.Button(frame,text='4',padx=20,pady=15,command=lambda: myclick(4),bg='#8fbc8f',border=4)
b4.grid(row=2,column=0)
b5=tk.Button(frame,text='5',padx=20,pady=15,command=lambda: myclick(5),bg='#ffebcd',border=4)
b5.grid(row=2,column=1)
b6=tk.Button(frame,text='6',padx=20,pady=15,command=lambda: myclick(6),bg='#ab4e52',border=4)
b6.grid(row=2,column=2)
b_sub=tk.Button(frame,text='-',padx=22,pady=15,command=sub,bg='#66cdaa',border=4)
b_sub.grid(row=2,column=3)

b7=tk.Button(frame,text='7',padx=20,pady=15,command=lambda: myclick(7),bg='#8fbc8f',border=4)
b7.grid(row=1,column=0)
b8=tk.Button(frame,text='8',padx=20,pady=15,command=lambda: myclick(8),bg='#8fbc8f',border=4)
b8.grid(row=1,column=1)
b9=tk.Button(frame,text='9',padx=20,pady=15,command=lambda: myclick(9),bg='#ffebcd',border=4)
b9.grid(row=1,column=2)
b_add=tk.Button(frame,text='+',padx=20,pady=15,command=add,bg='#66cdaa',border=4)
b_add.grid(row=1,column=3)

b0=tk.Button(frame,text='0',padx=20,pady=15,command=lambda: myclick(0),bg='#bc8f8f',border=4)
b0.grid(row=4,column=1)

b_equal=tk.Button(frame,text='=',padx=20,pady=15,command=equalto,bg='#e9d66b',border=4)
b_equal.grid(row=6,column=1)
b_clear=tk.Button(frame,text='clear',padx=30,pady=10,command=clr,bg='#5f9ea0',font=('bold'),border=4)
b_clear.grid(row=6,column=2,columnspan=2)

b_div=tk.Button(frame,text='/',padx=22,pady=15,command=div,bg='#66cdaa',border=4)
b_div.grid(row=4,column=3)
b_per=tk.Button(frame,text='%',padx=20,pady=15,command=prcnt,bg='#e9d66b',border=4)
b_per.grid(row=4,column=0)
b_sqrt=tk.Button(frame,text='√',padx=20,pady=15,command=sqt,bg='#5f9ea0',border=4)
b_sqrt.grid(row=4,column=2)
b_sqr=tk.Button(frame,text='x^y',padx=15,pady=15,command=square,bg='#5f9ea0',border=4)
b_sqr.grid(row=6,column=0)

b_sin=tk.Button(frame,text='SIN',padx=15,pady=15,command=sin,bg='#5f9ea0',border=4)
b_sin.grid(row=5,column=0)
b_cos=tk.Button(frame,text='COS',padx=11,pady=15,command=cos,bg='#e9d66b',border=4)
b_cos.grid(row=5,column=1)
b_tan=tk.Button(frame,text='TAN',padx=11,pady=15,command=tan,bg='#5f9ea0',border=4)
b_tan.grid(row=5,column=2)
b_log=tk.Button(frame,text='LOG',padx=11,pady=15,command=log,bg='#5f9ea0',border=4)
b_log.grid(row=5,column=3)

window.mainloop()
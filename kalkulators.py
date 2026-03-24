from tkinter import*
from math import *
import tkinter as tk

mansLogs=Tk()
mansLogs.title("Kalkulators")

def btnClick(number):
    current=e.get()
    e.delete(0,END)
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)
    return 0

def vienads():
    global num2
    global num1
    global mathOp
    num2=(float(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0 
    e.delete(0,END)
    e.insert(0,str(result))
    return 0


    

    
def btnCommand(command):
        global number
        global mathOp
        global num1
        global num3 
        mathOp=command
        num1=(float(e.get()))
        e.delete(0,END)
        return 0

def Clear():
     e.delete(0,END)
     num1=0
     mathOp=""
     return 0






btn0=Button(mansLogs,text="0",padx="40",pady="20", command=lambda:btnClick(0))
btn1=Button(mansLogs,text="1",padx="40",pady="20", command=lambda:btnClick(1))
btn2=Button(mansLogs,text="2",padx="40",pady="20", command=lambda:btnClick(2))
btn3=Button(mansLogs,text="3",padx="40",pady="20", command=lambda:btnClick(3))
btn4=Button(mansLogs,text="4",padx="40",pady="20", command=lambda:btnClick(4))
btn5=Button(mansLogs,text="5",padx="40",pady="20", command=lambda:btnClick(5))
btn6=Button(mansLogs,text="6",padx="40",pady="20", command=lambda:btnClick(6))
btn7=Button(mansLogs,text="7",padx="40",pady="20", command=lambda:btnClick(7))
btn8=Button(mansLogs,text="8",padx="40",pady="20", command=lambda:btnClick(8))
btn9=Button(mansLogs,text="9",padx="40",pady="20", command=lambda:btnClick(9))
btnSum=Button(mansLogs,text="+",padx="40",pady="20", command=lambda:btnCommand("+"))
btnSub=Button(mansLogs,text="-",padx="40",pady="20", command=lambda:btnCommand("-"))
btnMul=Button(mansLogs,text="*",padx="40",pady="20", command=lambda:btnCommand("*"))
btnDiv=Button(mansLogs,text="/",padx="40",pady="20", command=lambda:btnCommand("/"))
btnC=Button(mansLogs,text="C",padx="40",pady="20", command=Clear)
btnEq=Button(mansLogs,text="=",padx="40",pady="20", command=vienads)
btnLog=Button(mansLogs,text="log",padx="40",pady="20")
btnPM=Button(mansLogs,text="+/-",padx="40",pady="20")


btnPM.grid(row=5,column=0)
btnEq.grid(row=5,column=3)
btn0.grid(row=5,column=1)
btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btnSum.grid(row=4,column=3)
btnSub.grid(row=3,column=3)
btnMul.grid(row=2,column=3)
btnDiv.grid(row=1,column=3)
btnC.grid(row=1,column=0)
btnLog.grid(row=5,column=2)

e=Entry(mansLogs,width=15,bd=10,font=("Arial black",20))
e.grid(row=0,column=0,columnspan=4)










mansLogs.mainloop()
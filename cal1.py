from sqlite3 import complete_statement
from tkinter import *
root = Tk()
root.title("Calculator")

content=""
txt_input= StringVar(value="0")

def btn(number):
    global content
    content=content+str(number)
    txt_input.set(content)

def equal():
    global content
    calculate=float(eval(content))
    txt_input.set(calculate)
    content= ""

def clear():
    global content
    content=""
    txt_input.set("")
    display.insert(0,"0")
#display
display = Entry(font=('arail',25,'bold'),fg="white",bg="black",textvariable=txt_input,justify="right")
display.grid(columnspan=4)

#button
#row1
btn7=Button(fg="Black",font=('arail',25,'bold'),text="7",command=lambda:btn(7),padx=25,pady=15).grid(row=1,column=0)
btn8=Button(fg="Black",font=('arail',25,'bold'),text="8",command=lambda:btn(8),padx=25,pady=15).grid(row=1,column=1)
btn9=Button(fg="Black",font=('arail',25,'bold'),text="9",command=lambda:btn(9),padx=25,pady=15).grid(row=1,column=2)
btnc=Button(fg="Black",bg="gray",font=('arail',25,'bold'),command=clear,text="C",padx=27,pady=15).grid(row=1,column=3)
#row2
btn4=Button(fg="Black",font=('arail',25,'bold'),text="4",command=lambda:btn(4),padx=25,pady=15).grid(row=2,column=0)
btn5=Button(fg="Black",font=('arail',25,'bold'),text="5",command=lambda:btn(5),padx=25,pady=15).grid(row=2,column=1)
btn6=Button(fg="Black",font=('arail',25,'bold'),text="6",command=lambda:btn(6),padx=25,pady=15).grid(row=2,column=2)
btnpuls=Button(fg="Black",bg="gray",font=('arail',25,'bold'),text="+",command=lambda:btn("+"),padx=30,pady=15).grid(row=2,column=3)
#row3
btn1=Button(fg="Black",font=('arail',25,'bold'),text="1",command=lambda:btn(1),padx=25,pady=15).grid(row=3,column=0)
btn2=Button(fg="Black",font=('arail',25,'bold'),text="2",command=lambda:btn(2),padx=25,pady=15).grid(row=3,column=1)
btn3=Button(fg="Black",font=('arail',25,'bold'),text="3",command=lambda:btn(3),padx=25,pady=15).grid(row=3,column=2)
btnminus=Button(fg="Black",bg="gray",font=('arail',25,'bold'),text="-",command=lambda:btn("-"),padx=35,pady=15).grid(row=3,column=3)
#row4
btn0=Button(fg="Black",font=('arail',25,'bold'),text="0",command=lambda:btn(0),padx=25,pady=15).grid(row=4,column=1)
btndot=Button(fg="Black",font=('arail',25,'bold'),text=".",command=lambda:btn("."),padx=30,pady=15).grid(row=4,column=0)
btndivision=Button(fg="Black",bg="gray",font=('arail',25,'bold'),text="÷",command=lambda:btn("/"),padx=25,pady=15).grid(row=4,column=2)
btnmultiply=Button(fg="Black",bg="gray",font=('arail',25,'bold'),text="x",command=lambda:btn("*"),padx=32,pady=15).grid(row=4,column=3)
#row5
btnequal=Button(fg="white",bg="black",font=('arail',25,'bold'),text="=",command=equal,padx=25,pady=15).grid(row=5,column=0)
btnopen=Button(fg="Black",bg="gray",font=('arail',25,'bold'),text="(",command=lambda:btn("("),padx=35,pady=15).grid(row=5,column=1)
btnclose=Button(fg="Black",bg="gray",font=('arail',25,'bold'),text=")",command=lambda:btn(")"),padx=35,pady=15).grid(row=5,column=2)
root.mainloop()
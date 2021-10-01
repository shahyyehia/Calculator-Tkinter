from tkinter import *
main=Tk()
main.resizable(False,False)
main.config(bg="black")
main.sign="none"
main.length=0
main.number1=0
main.number2=0
def zero():
    space["text"]=space["text"]+"0"
def one():
    space["text"]=space["text"]+"1"
def two():
    space["text"]=space["text"]+"2"
def three():
    space["text"]=space["text"]+"3"
def four():
    space["text"]=space["text"]+"4"
def five():
    space["text"]=space["text"]+"5"
def six():
    space["text"]=space["text"]+"6"
def seven():
    space["text"]=space["text"]+"7"
def eight():
    space["text"]=space["text"]+"8"
def nine():
    space["text"]=space["text"]+"9"
def plus():
    main.number1=int(space["text"])
    main.length=len(space["text"])
    space["text"] = space["text"] + "+"
    main.sign="plus"
def minus():
    main.number1=int(space["text"])
    main.length=len(space["text"])
    space["text"] = space["text"] + "-"
    main.sign="minus"

def multiply():
    main.number1=int(space["text"])
    main.length=len(space["text"])
    space["text"] = space["text"] + "*"
    main.sign="multiply"
def divide():
    main.number1=int(space["text"])
    main.length=len(space["text"])
    space["text"] = space["text"] + "/"
    main.sign="divide"
def delete():
    space["text"] = " "
def equal():
    if main.sign=="plus":
        main.number2=int(space["text"][main.length+1:])
        space["text"] = main.number1+main.number2
    elif main.sign=="minus":
        main.number2=int(space["text"][main.length+1:])
        space["text"] = main.number1-main.number2
    elif main.sign=="divide":
        main.number2=int(space["text"][main.length+1:])
        space["text"] = main.number1/main.number2
    elif main.sign=="multiply":
        main.number2=int(space["text"][main.length+1:])
        space["text"] = main.number1*main.number2

space=Label(main,text=" " ,bg="white",width=30,height=5,font=("helvetical",10,"bold"))
space.grid(row=0,column=0,columnspan=4)
one=Button(main,text="1",bg="black",fg="white",width=7,height=3,command=one)
one.grid(row=1,column=0,padx=0,pady=0)
two=Button(main,text="2",bg="black",fg="white",width=7,height=3,command=two)
two.grid(row=1,column=1,padx=0,pady=0)
three=Button(main,text="3",bg="black",fg="white",width=7,height=3,command=three)
three.grid(row=1,column=2,padx=0,pady=0)
plus=Button(main,text="+",bg="black",fg="white",width=7,height=3,command=plus)
plus.grid(row=1,column=3,padx=0,pady=0)
four=Button(main,text="4",bg="black",fg="white",width=7,height=3,command=four)
four.grid(row=2,column=0,padx=0,pady=0)
five=Button(main,text="5",bg="black",fg="white",width=7,height=3,command=five)
five.grid(row=2,column=1,padx=0,pady=0)
six=Button(main,text="6",bg="black",fg="white",width=7,height=3,command=six)
six.grid(row=2,column=2,padx=0,pady=0)
minus=Button(main,text="-",bg="black",fg="white",width=7,height=3,command=minus)
minus.grid(row=2,column=3,padx=0,pady=0)
seven=Button(main,text="7",bg="black",fg="white",width=7,height=3,command=seven)
seven.grid(row=3,column=0,padx=0,pady=0)
eight=Button(main,text="8",bg="black",fg="white",width=7,height=3,command=eight)
eight.grid(row=3,column=1,padx=0,pady=0)
nine=Button(main,text="9",bg="black",fg="white",width=7,height=3,command=nine)
nine.grid(row=3,column=2,padx=0,pady=0)
multiply=Button(main,text="x",bg="black",fg="white",width=7,height=3,command=multiply)
multiply.grid(row=3,column=3,padx=0,pady=0)
zero=Button(main,text="0",bg="black",fg="white",width=7,height=3,command=zero)
zero.grid(row=4,column=0,padx=0,pady=0)
delete=Button(main,text="c",bg="black",fg="white",width=7,height=3,command=delete)
delete.grid(row=4,column=1,padx=0,pady=0)
divide=Button(main,text="/",bg="black",fg="white",width=7,height=3,command=divide)
divide.grid(row=4,column=2,padx=0,pady=0)
equals=Button(main,text="=",bg="black",fg="white",width=7,height=3,command=equal)
equals.grid(row=4,column=3,padx=0,pady=0)
main.mainloop()
import tkinter as tk 
from PIL import ImageTk
w=tk.Tk()
global s1,s2,s3
s1=tk.StringVar()
s2=tk.StringVar()
s3=tk.StringVar()
def window():
    w.title('Simple and Compound intrest')
    w.geometry('1300x700+0+0')
    w.resizable(True,True)
    w.configure(bg='skyblue')
def calculate():
    global entry1,entry2,entry3,result
    p=s1.get()
    r=s2.get()
    t=s3.get()
    SI=(float(p)*float(r)*float(t))/100
    final="{:.3f}".format(SI)
    result.insert(0,str(final))
def resetcommand():
     entry1.delete(0,'end')
     entry2.delete(0,'end')
     entry3.delete(0,'end')
     result.delete(0,'end')
def design():
    global entry1,entry2,entry3,result
    photo=ImageTk.PhotoImage(file="sc.png")
    l1=tk.Label(w,image=photo)
    l1.place(x=600,y=150)
    l2=tk.Label(w,text="SIMPLE INTREST CALCULATOR",font=('impact',30,'bold'),bg='skyblue')
    l2.place(x=400,y=40)
    #principle
    principle=tk.Label(w,text="Principle:",font=('microsoft yahi ui light',20,'bold'),bg='skyblue',fg='green')
    principle.place(x=80,y=120)
    entry1=tk.Entry(w,font=('microsoft yahi ui light',20,'bold'),bd=0,width=20,textvariable=s1)
    entry1.place(x=80,y=160)
    #rate
    rate=tk.Label(w,text="Rate:",font=('microsoft yahi ui light',20,'bold'),bg='skyblue',fg='green')
    rate.place(x=80,y=250)
    entry2=tk.Entry(w,font=('microsoft yahi ui light',20,'bold'),bd=0,width=20,textvariable=s2)
    entry2.place(x=80,y=290)
    #time
    time=tk.Label(w,text="Time:",font=('microsoft yahi ui light',20,'bold'),bg='skyblue',fg='green')
    time.place(x=80,y=390)
    entry3=tk.Entry(w,font=('microsoft yahi ui light',20,'bold'),bd=0,width=20,textvariable=s3)
    entry3.place(x=80,y=430)
    #button
    button=tk.Button(w,bd=0,width=11,text="Calculate",fg='white',bg='blue',font=("microsoft yahi ui light",15,'bold'),command=calculate)
    button.place(x=80,y=510)
    #reset button
    reset=tk.Button(w,text="Reset",font=("microsoft yahi ui light",15,'bold'),fg="white",bg="red",width=11,bd=0,command=resetcommand)
    reset.place(x=250,y=510)
    #lable result
    result=tk.Entry(w,font=("microsoft yahi ui light",20,'bold'),bg='white',bd=0,width=30)
    result.place(x=50,y=600)
    w.mainloop()
#main
window()
design()
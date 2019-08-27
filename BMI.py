from tkinter import *
import sqlite3

conn = sqlite3.connect('BMI.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS BMI (Name TEXT,AGE TEXT,PHN TEXT, BMI TEXT)')
root = Tk()
root.geometry("1350x800+0+0")
root.resizable(0,0)
root.title("BMI")

var1 = DoubleVar() #weight
var2 = DoubleVar() #height
var3 = DoubleVar() #convert
var4 = StringVar() #name
var5 = IntVar()    #age
var6 = StringVar() #phone
ans = StringVar() #bmi answer

def BMI_CAL():
    Bheight = float(var2.get())
    Bweight = float(var1.get())
    BMI = str('%.2f' %(Bweight / (Bheight * Bheight)))
    ans=BMI
    lblBMIResult.config(text=BMI)
    named = var4.get()
    aged = var5.get()
    phno = var6.get()
    c.execute('INSERT INTO BMI (Name ,AGE, PHN,BMI) VALUES(?,?,?,?)', (named, aged, phno,ans))
    conn.commit()

def Conver():
    inches = float(var3.get())
    Metres= str('%.2f' %(inches * 0.3048))
    Convert.config(text=Metres)

def Clear():
    N1.delete(0,'end')
    A1.delete(0,'end')
    D1.delete(0,'end ')
    conv1.delete(0,'end')
    txtheight.delete(0,END)

Tops = Frame(root, width= 1350, height= 50, bd= 8, relief="raise")
Tops.pack(side=TOP)
f1 = Frame(root, width= 600, height= 600, bd= 8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width= 300, height= 700, bd= 8, relief="raise")
f2.pack(side=RIGHT)

f1a= Frame(f1, width= 600, height= 200, bd= 20, relief="raise")
f1a.pack(side=TOP)
f1b= Frame(f1, width= 600, height= 10, bd= 20, relief="raise")
f1b.pack(side=TOP)
f1c= Frame(f1, width= 600, height= 200, bd= 20, relief="raise")
f1c.pack(side=TOP)


f2a= Frame(f2, width= 600, height= 200, bd= 20, relief="raise")
f2a.pack(side=TOP)
f2b= Frame(f2, width= 600, height= 10, bd= 20, relief="raise")
f2b.pack(side=TOP)

lblTitle=Label(Tops, text="         BMI         ", padx=16, pady=16, bd=16, font=('arial',20,'bold'), bg="yellow" ,relief= "raise",width=80,height= 1)
lblTitle.pack()

lblweight= Label(f1a, text="Select weight in kilograms",font=('arial',20,'bold'), bd=5).grid(row = 0, column= 0)
Bodyweight = Scale(f1a, variable= var1, from_= 1 , to = 200, length= 880,tickinterval= 30,orient = HORIZONTAL)
Bodyweight.grid(row = 1, column= 0)

lblheight= Label(f1b, text="Select Height in Meters",font=('arial',20,'bold'), bd=10).grid(row = 0, column= 0)
txtheight = Entry(f1b, textvariable= var2,font=('arial',20,'bold'), bd=5, width=22)
txtheight.grid(row = 1, column= 0)

lblBMIResult = Label( f1b, padx=46, pady=16 ,bd=10, font=('arial',16,'bold'), bg="sky blue", relief="sunk", width=20, height=1)
lblBMIResult.grid(row= 2, column=0)

lblconv= Label(f1c, text="Convert Foot to Meters",font=('arial',15,'bold'), bd=10).grid(row = 0, column= 0)
conv1=Entry(f1c,textvariable= var3 ,font=('arial',20,'bold'), bd=5, width=5)
conv1.grid(row = 1, column= 0)

Convert= Label( f1c,bd=5, font=('arial',16,'bold'), bg="wheat", relief="sunk", width=8, height=2)
Convert.grid(row= 1, column=2)

lblBMITable= Label(f2b,font=('arial',15,'bold'),text="BMI TABLE").grid(row= 0,column= 0)
txtlblBMITable= Text(f2b, height= 12, width= 38, bd =8,font=('arial',11,'bold') )
txtlblBMITable.grid(row=1, column= 0)

txtlblBMITable.insert(END , 'Meaning\t\t' + "BMI \n\n")
txtlblBMITable.insert(END , 'normal weigth \t\t' + "19-24\n\n")
txtlblBMITable.insert(END , 'overweight \t\t' + "25-29\n\n")
txtlblBMITable.insert(END , 'obesity I\t\t' + "30-34\n\n")
txtlblBMITable.insert(END , 'obesity II\t\t' + "35-34\n\n")
txtlblBMITable.insert(END , 'obesity III\t\t' + "> 40\n\n")

NAMES= Label(f2a, text="NAME ==>",font=('arial',11,'bold'), bd=10,  width=10).grid(row = 1, column= 0)
N1=Entry(f2a,textvariable= var4,font=('arial',8,'bold'), bd=2, width=30)
N1.grid(row = 1, column= 1)

Ages= Label(f2a, text="AGE ==>",font=('arial',11,'bold'), bd=10,  width=10).grid(row = 2, column= 0)
A1=Entry(f2a,textvariable= var5,font=('arial',8,'bold'), bd=2, width=30)
A1.grid(row = 2, column= 1)

DOB= Label(f2a, text="Phone No ==>",font=('arial',11,'bold'), bd=10,  width=10).grid(row = 3, column= 0)
D1=Entry(f2a,textvariable= var6,font=('arial',8,'bold'), bd=2, width=29)
D1.grid(row = 3, column= 1)

btnclear= Button(f2a, text= "Clear",padx=8, pady=8, bd=8, width=8,font=('arial',10,'bold'),height=1, command = Clear)
btnclear.grid(row=4,column=0)

btnBMI= Button(f2b, text= "SUBMIT",padx=8, pady=8, bd=12, width=15,font=('arial',15,'bold'),height=1,command=BMI_CAL)
btnBMI.grid(row=2,column=0)

btncon= Button(f1c, text= "Convert", bd=10, width=12,font=('arial',10,'bold'),height=2, command=Conver)
btncon.grid(row=1,column=3)

root.mainloop()
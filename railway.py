from tkinter import*
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox




root = Tk()
root.geometry("1350x750+0+0")
root.title("train ticket")
root.configure(background='black')

Tops = Frame(root,width=1350, height=100, bd=14, relief='raise')
Tops.pack(side=TOP)

f1 = Frame(root,width=900, height=650, bd=8, relief='raise')
f1.pack(side=LEFT)
f2 = Frame(root,width=440, height=100, bd=8, relief='raise')
f2.pack(side=RIGHT)

frametopRight = Frame(f2, width=440, height=650, bd=12, relief='raise')
frametopRight.pack(side=TOP)
frameBottomRight = Frame(f2, width=440, height=50, bd=16, relief='raise')
frameBottomRight.pack(side=BOTTOM)

f1a = Frame(f1, width=900, height=330, bd=8, relief='raise')
f1a.pack(side=TOP)
f2a= Frame(f1, width=900, height=320, bd=6, relief='raise')
f2a.pack(side=BOTTOM)

topLeft1 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
topLeft1.pack(side=LEFT)
topLeft2 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
topLeft2.pack(side=RIGHT)
topLeft3 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
topLeft3.pack(side=RIGHT)
#---------------------------------------------------------

bottomLeft1 = Frame(f2a, width = 450, height = 450, bd = 14, relief="raise")
bottomLeft1.pack(side=LEFT)

bottomLeft2 = Frame(f2a, width = 450, height = 450, bd = 14, relief="raise")
bottomLeft2.pack(side=RIGHT)
#------------------------------------------------------------------------------
Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
lb1Title=Label(Tops, font=('arial',40, 'bold'),text="Train ticket system",bd=10, width=41, justify='center')
lb1Title.grid(row=0,column=0)

Date1 = StringVar()
time1 = IntVar()
Ticketclass = StringVar()
TicketPrice = StringVar()
Child_Ticket = StringVar()
Adult_Ticket = StringVar()
From_Destination = StringVar()
To_Destination = StringVar()
Fee_Price = StringVar()
Route=StringVar()
Receipt_Ref  = StringVar()

Ticketclass.set("")
TicketPrice.set("")
Child_Ticket.set("")
Adult_Ticket.set("")
From_Destination.set("")
#To_Destination("")
Route.set("")
Receipt_Ref.set("")

#------------------------------------------------------------------------------
lb1Receipt=Label(frametopRight, font=('arial',18, 'bold'),text="\nTrevelling ticketing system\n",bd=10, width=25, justify='center')
lb1Receipt.grid(row=0,column=0)

lb1Class1=Label(frameBottomRight, font=('arial',14, 'bold'),text="Class", width=8,relief = 'sunken', justify='center')
lb1Class1.grid(row=0,column=0)
lb1Class2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief = 'sunken', justify='center')
lb1Class2.grid(row=1,column=0)

lb1Ticket1=Label(frameBottomRight, font=('arial',14, 'bold'),text="Ticket", width=8,relief = 'sunken', justify='center')
lb1Ticket1.grid(row=0,column=1)
lb1Ticket2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief = 'sunken', justify='center')
lb1Ticket2.grid(row=1,column=1)

lb1Adult1=Label(frameBottomRight, font=('arial',14, 'bold'),text="Adult", width=8,relief = 'sunken', justify='center')
lb1Adult1.grid(row=0,column=2)
lb1Adult2=Label(frameBottomRight, font=('arial',14, 'bold'),text="Adult", width=8,relief = 'sunken', justify='center')
lb1Adult2.grid(row=1,column=2)

lb1Child1=Label(frameBottomRight, font=('arial',14, 'bold'),text="Child", width=8,relief = 'sunken', justify='center')
lb1Child1.grid(row=0,column=3)
lb1Child2=Label(frameBottomRight, font=('arial',14, 'bold'),text="Child", width=8,relief = 'sunken', justify='center')
lb1Child2.grid(row=1,column=3)
#-----------------------------------------
lb1sp=Label(frameBottomRight,font=('arial',14,'bold'),width=34,height=2,relief = 'sunken',justify='center')
lb1sp.grid(row=2,column=0,columnspan=4)
#-----------------------------------------
lb1From1=Label(frameBottomRight, font=('arial',14, 'bold'),text="From", width=8,relief = 'sunken', justify='center')
lb1From1.grid(row=3,column=1)
lb1From2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief = 'sunken', justify='center')
lb1From2.grid(row=3,column=2)
#------------------------------------------spacing-

lb1To1=Label(frameBottomRight, font=('arial',14, 'bold'),text="To", width=8,relief = 'sunken', justify='center')
lb1To1.grid(row=4,column=1)
lb1To2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief = 'sunken', justify='center')
lb1To2.grid(row=4,column=2)

lb1Price1=Label(frameBottomRight, font=('arial',14, 'bold'),text="Price", width=8,relief = 'sunken', justify='center')
lb1Price1.grid(row=5,column=1)
lb1Price2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief = 'sunken', justify='center')
lb1Price2.grid(row=5,column=2)
#------------------------------------------specing-
lb1sp=Label(bottomLeft1,font=('arial',14,'bold'),width=34,height=2,relief = 'sunken',justify='center')
lb1sp.grid(row=6,column=0,columnspan=4)
#------------------------------------------

lb1RefNo1=Label(frameBottomRight, font=('arial',14, 'bold'),text="RefNo", width=8,relief = 'sunken', justify='center')
lb1RefNo1.grid(row=5,column=0)
lb1RefNo2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief = 'sunken', justify='center')
lb1RefNo2.grid(row=6,column=0)

lb1Time1=Label(frameBottomRight, font=('arial',14, 'bold'),text="Time", width=8,relief = 'sunken',textvariable=time1, justify='center')
lb1Time1.grid(row=5,column=1)
lb1Time2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief = 'sunken', justify='center')
lb1Time2.grid(row=6,column=1)

lb1Date1=Label(frameBottomRight, font=('arial',14, 'bold'),text="Date", width=8,relief = 'sunken', justify='center')
lb1Date1.grid(row=5,column=2)
lb1Date2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief = 'sunken',textvariable=Date1, justify='center')
lb1Date2.grid(row=6,column=2)

lb1Route1=Label(frameBottomRight, font=('arial',14, 'bold'),text="Route", width=8,relief = 'sunken', justify='center')
lb1Route1.grid(row=5,column=3)
lb1Route2=Label(frameBottomRight, font=('arial',14, 'bold'), width=8,relief = 'sunken', justify='center')
lb1Route2.grid(row=6,column=3)

#-----------------------------------------function-------------------------------------
def btnClick(numbers):
    global operator
    operator = operator  + str(numbers)
    text_Input.set(operator)
   
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
   
def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator=""
def iExit():
    qExit= massgebox.askyesno('quit system','do you want to Quit?')
    if qExit > 0:
        root.destroy()
        return
def Travel_cost():
    if (var9.get() =="chennai" and var1.get() == 1 and var4.get() == 1 ):
        Tcost = float(30.8)
        Single = float(var12.get())
        Adult_Tax = "$",str('%.2f'%((Tcost*Single)*0.03))
        Adult_Fees = "$",str('%.2f'%(Tcost*Single))
        TotalCost = "$",str('%.2f'%((Tcost*Single) + ((Tcost*Single)*0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("standard")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set('vashi')
        #To_Destination.set("varanasi")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")
       
        x = random.randint(109, 5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)
       
    elif (var9.get() == "varanasi" and var1.get() == 1 and var5.get() == 1 ):
        Tcost = float(75)
        Single = float(var12.get())
        Child_Tax ="$",str('%.2f'%(Tcost *0))
        Child_Fees = "$",str('%.2f'%(Tcost*Single))
        TotalCost = "$",str('%.2f'%((Tcost*Single) + (Tcost * 0)))
        Tax.set(child_Tax_Tax)
        SubTotal.set(Child_Fees)
        Ticketclass.set("standard")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set('vashi')
        #To_Destination.set("varanasi")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Rout.set("Direct")
       
        x = random.randint(109, 5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL"+randomRef)
def Checkbutton_Value():
    if (var10.get() == 1):
        var12.set("")
        entSingle.configure(state=NORMAL)
    elif var10.get()== 0:
        entSingle.configure(state=DISABLED)
        var12.set("0")
    if (var11.get() == 1):
        var6.set("")
        entReturn.configure(state=NORMAL)
    elif var11.get() == 0:
        entReturn.configure(state=DISABLED)
        var6.set("0")
           
       
   
def Reset():
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    Total.set("0")
    SubTotal.set("0")
    Ticketclass.set("")
    TicketPrice.set("")
    Adult_Ticket.set("")
    Child_Ticket.set("")
    From_Destination.set("")
    #To_Destination.set("")
    Fee_Price.set("")
   
#--------------------------variable-------------------
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
Tax =   IntVar()

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
#To_Destination("0")

SubTotal = StringVar()
Total = StringVar()
text_Input = StringVar()
operator = ""
#--------------------------------------------ticket-------------------------------------------------
Date1.set(time.strftime("%d/%n/%y"))
time1.set(time.strftime("%H:%M:%S"))
#--------------------------create weight topLeft1-------------------
lb1Class = Label(topLeft1, font=('arial',22, 'bold'),text='class',bd=8)
lb1Class.grid(row=0,column=0,sticky=W)
chkStandard = Checkbutton(topLeft1, font=('arial',20,'bold'), text='standard',variable=var1, onvalue=1, offvalue=0)
chkStandard.grid(row=1, column=0, sticky=W)
chkEconomy = Checkbutton(topLeft1, font=('arial',20,'bold'), text='Economy',variable=var2, onvalue=1, offvalue=0)
chkEconomy.grid(row=2, column=0, sticky=W)
chkFirstclass = Checkbutton(topLeft1, font=('arial',20,'bold'), text='First class',variable=var3, onvalue=1, offvalue=0)
chkFirstclass.grid(row=3, column=0, sticky=W)
#--------------------------create weight topLeft2-------------------

lblSelect = Label(topLeft3, font=('arial',22, 'bold'),text='select A destination',bd=8)
lblSelect.grid(row=0,column=0,sticky=W, columnspan=2)
lblDestination = Label(topLeft3, font=('arial',20, 'bold'),text='destination',bd=2)
lblDestination.grid(row=1,column=0,sticky=W)
cboDestination =ttk.Combobox(topLeft3, textvariable = var9, state='readonly',font=('arial',20,'bold'),width=8)
cboDestination['value']=('','varanasi','vashi','chennai','nagpur')
cboDestination.current(0)
cboDestination.grid(row=1,column=1)

chkAdult = Checkbutton(topLeft3, font=('arial',20,'bold'), text='Adult',variable=var4, onvalue=1, offvalue=0)
chkAdult.grid(row=2, column=0, sticky=W)
chkchild= Checkbutton(topLeft3, font=('arial',20,'bold'), text='child',variable=var5, onvalue=1, offvalue=0)
chkchild.grid(row=3, column=0, sticky=W)

#--------------------------------------------ticket-------------------------------------------------
lb1Class = Label(topLeft2, font=('arial',22, 'bold'),text='ticket Type',bd=8)
lb1Class.grid(row=0,column=0,sticky=W)
chkSingle = Checkbutton(topLeft2, font=('arial',20,'bold'), text='Single',variable=var10, onvalue=1, offvalue=0)
chkSingle.grid(row=1, column=0, sticky=W)
entSingle = Entry(topLeft2, font=('arial',20,'bold'), textvariable = var5, width=8)
entSingle.grid(row=1, column=0, sticky=W)
chkReturn = Checkbutton(topLeft2, font=('arial',20,'bold'), text='return',variable=var11, onvalue=1, offvalue=0)
chkReturn.grid(row=2, column=0, sticky=W)
entReturn = Entry(topLeft2, font=('arial',20,'bold'), textvariable = var6, width=8)
entReturn.grid(row=1, column=0, sticky=W)
lb1Comment = Label(topLeft2, font=('arial',22, 'bold'),text='comment',bd=8)
lb1Comment.grid(row=3,column=0,sticky=W)
entComment= Entry(topLeft2, font=('arial',20,'bold'), textvariable = var7,bd=2, width=8)
entComment.grid(row=3, column=1, sticky=W)

#-----------------------------------calculator------------------------------------------------------

text_Input=StringVar()
txtDisplay = Entry(bottomLeft2,font=('arial',10,'bold'),textvariable=text_Input,bd=16,justify='right',width=36)
txtDisplay.grid(columnspan=4)

btn7=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='7',bg='powder blue',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='8',bg='powder blue',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='9',bg='powder blue',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAddition=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='+',bg='powder blue',command=lambda:btnClick('+')).grid(row=2,column=3)

#-------------------------------------------------------------------------------------------------------

btn4=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='4',bg='powder blue',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='5',bg='powder blue',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='6',bg='powder blue',command=lambda:btnClick(6)).grid(row=3,column=2)
Subtraction=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='-',bg='powder blue',command=lambda:btnClick('-')).grid(row=3,column=3)

#-------------------------------------------------------------------------------------------------------

btn1=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='1',bg='powder blue',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='2',bg='powder blue',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='3',bg='powder blue',command=lambda:btnClick(3)).grid(row=4,column=2)
multiply=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='*',bg='powder blue',command=lambda:btnClick('*')).grid(row=4,column=3)

#-------------------------------------------------------------------------------------------------------------------

btn0=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='0',bg='powder blue',command=lambda:btnClick(0)).grid(row=5,column=0)
clear=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='C',bg='powder blue',command=lambda:btnClick('C')).grid(row=5,column=1)
equal=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='=',bg='powder blue',command=lambda:btnClick('=')).grid(row=5,column=2)
division=Button(bottomLeft2,padx=8,pady=8,bd=8,fg='black',font=('arial',10,'bold'),text='/',bg='powder blue',command=lambda:btnClick('/')).grid(row=5,column=3)

#------------------------------------------tax, subtotaland total-------------------------------------------------------------------------

lb1StateTax = Label(bottomLeft1,font=('arial',24,'bold'),text="state Tax",bd=16, anchor='w')
lb1StateTax.grid(row=3,column=2)

txtStateTax = Entry(bottomLeft1,font=('arial',16,'bold'),textvariable=Tax,bd=10,width=28,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)
lb1SubTotal = Label(bottomLeft1,font=('arial',24,'bold'),text="sub total",bd=16,anchor='w')
lb1SubTotal.grid(row=4,column=2)

txtSubTotal = Entry(bottomLeft1,font=('arial',16,'bold'),textvariable=Tax,bd=10,width=28,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)
lb1TotalCost = Label(bottomLeft1,font=('arial',24,'bold'),text="sub total",bd=16,anchor='w')
lb1TotalCost.grid(row=5,column=2)
txtTotalCost = Entry(bottomLeft1,font=('arial',16,'bold'),textvariable=Tax,bd=10,width=28,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)
#-------------------------------------------------spacing-------------------------------------------------
lb1sp=Label(bottomLeft1,font=('arial',24,'bold'),width=44,height=2,relief = 'sunken',justify='center')
lb1sp.grid(row=9,column=0,columnspan=4)
#-------------------------------------------------------------------------------------------------------------------
lb1Space = Label(bottomLeft1,font=('arial',24,'bold'),text="       \n     ",bd=16, anchor='w')
lb1Space.grid(row=6,column=2)
#-----------------
lb1Space = Label(bottomLeft1,font=('arial',24,'bold'),text="    \n     ",bd=16, anchor='w')
lb1Space.grid(row=6,column=4)
#---------------------------------------space--------------------------------------------------------
lb1sp=Label(bottomLeft1,font=('arial',24,'bold'),width=44,height=2,relief = 'sunken',justify='center')
lb1sp.grid(row=9,column=0,columnspan=4)


#------------------------------------------------button-------------------------------------------------------------------

btnTotal = Button(frameBottomRight,text='convert',padx=2,pady=2,bd=2,fg='black',font=('arial',12,'bold'),width= 6,height=1 ).grid(row=7,column=0)
btnClear = Button(frameBottomRight,text='Clear',padx=2,pady=2,bd=2,fg='black',font=('arial',12,'bold'),width= 6,height=1,command=Reset ).grid(row=7,column=1)
btnReset = Button(frameBottomRight,text='Reset',padx=2,pady=2,bd=2,fg='black',font=('arial',12,'bold'),width= 6,height=1,command=Reset ).grid(row=7,column=2)

btnExit = Button(frameBottomRight,text='Exit',padx=2,pady=2,bd=2,fg='black',font=('arial',12,'bold'),width= 6,height=1, command= iExit).grid(row=7,column=3)
#--------------------------space
lb1sp=Label(frameBottomRight,font=('arial',14,'bold'),width=34,height=2,relief = 'sunken',justify='center')
lb1sp.grid(row=11,column=0,columnspan=4)

root.mainloop()

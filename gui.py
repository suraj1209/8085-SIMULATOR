from tkinter import *
import sys
import os
import tkinter.messagebox
import main
import register
import parse
import tkinter.simpledialog as simpledialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showerror
from tkinter.messagebox import *
from tkinter.filedialog import *

#*****************************************************************************TKINTER WINDOW***************************************************************************
file=None
root=Tk()
root.geometry("1280x675+00+0")
root.title("8085 SIMULATOR")

#*****************************************************************************FRAME*************************************************************************************

frame1 = Frame(root, width=140, height=220, bd=3, relief="groove")
frame1.place(x=850, y=45)
frame2 = Frame(root, width=150, height=220, bd=3, relief="groove")
frame2.place(x=1050, y=45)

#*********************************************************************MENUBAR FUNCTIONALITY****************************************************************************

def openFile():
        global file 
        file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
 
        if file == "":
            file = None

        else:
            root.title(os.path.basename(file) + " - Notepad")
            txtarea.delete(1.0,END)
 
            f = open(file,"r")
 
            txtarea.insert(1.0,f.read())
 
            f.close()

def NewFile():
    global file
    root.title("untitled - TextPad")
    file=None
    txtarea.delete('1.0','end')

def Save():
    global file
    if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
 
            if file == "":
                file = None
            else:
                f = open(file,"w")
                f.write(txtarea.get(1.0,END))
                f.close()
                root.title(os.path.basename(file) + " - Notepad")
                 
             
    else:
        f = open(file,"w")
        f.write(txtarea.get(1.0,END))
        f.close()

def reset_flag():
    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')

def reset_register():
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')

def exit_window():
        global file
        p=0
        if file==None or file=="":
                t1=txtarea.get('1.0','end-1c')
                if t1=="":
                        root.destroy()
                else:
                        p=askquestion("Exit","Are you sure you want to exit without saving",icon='warning')
                if p=="yes":
                        root.destroy()
                        
        else:
                f=open(file,"r")
                txt1=f.read()
                text=txtarea.get('1.0','end')
                if txt1==text:
                        root.destroy()
                else:
                        p=askquestion("Exit","Are you sure you want to exit without saving",icon='warning')
                        if p=="yes":
                                root.destroy()

def open_tut():
    import webbrowser
    webbrowser.open("tutorial.txt", 'r')

def smp_prog():
        import webbrowser
        webbrowser.open("Sample.txt",'r')
    
    
#*****************************************************************************MENU BAR*********************************************************************************

menu=Menu(root, bg="blue")
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open...", command=openFile, font=("Helvetica",10), accelerator="ctrl+O")
root.bind('<Control-o>', lambda e: openFile())
subMenu.add_command(label="Save...", command=Save, font=("Helvetica",10), accelerator="ctrl+S")
root.bind('<Control-s>', lambda e: Save())
subMenu.add_command(label="New File", command=NewFile, font=("Helvetica",10), accelerator="ctrl+N")
root.bind('<Control-n>', lambda e: NewFile())
subMenu.add('separator')
subMenu.add_command(label="Quit", command=exit_window, font=("Helvetica",10), accelerator="ctrl+Q")
root.bind('<Control-q>', lambda e: exit_window())
root.bind('<Alt-F4>', lambda e: exit_window())
subMenu.add('separator')

helpMenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="Tutorial", command=open_tut, font=("Helvetica",10), accelerator="ctrl+H")
helpMenu.add('separator')
root.bind('<Control-h>', lambda e: open_tut())
helpMenu.add_command(label="Sample Program", command=smp_prog, font=("Helvetica",10), accelerator="ctrl+P")
helpMenu.add('separator')
root.bind('<Control-p>', lambda e: smp_prog())

root.protocol("WM_DELETE_WINDOW", exit_window)

#*************************************************************************************DEFINING LABELS*******************************************************************

l1=Label(text="ENTER YOUR CODE HERE", font=("Helvetica", 16))
l2=Label(root, text="FLAGS:", font=("Helvetica", 12))
l3=Label(root, text="Sign:", font=("Helvetica", 12), fg="brown")
l4=Label(root, text="Zero:", font=("Helvetica", 12), fg="brown")
l5=Label(root, text="Aux Carry:", font=("Helvetic", 12), fg="brown")
l6=Label(root, text="Parity:", font=("Helvetica", 12), fg="brown")
l7=Label(root, text="Carry:", font=("Helvetica", 12), fg="brown")
l8=Label(root, text="REGISTERS:", font=("Helvetica", 12))
l9=Label(root, text="Reg A:", font=("Helvetica", 12), fg="brown")
l10=Label(root, text="Reg B:", font=("Helvetica", 12), fg="brown")
l11=Label(root, text="Reg C:", font=("Helvetica", 12), fg="brown")
l12=Label(root, text="Reg D:", font=("Helvetica", 12), fg="brown")
l13=Label(root, text="Reg E:", font=("Helvetica", 12), fg="brown")
l14=Label(root, text="Reg H:", font=("Helvetica", 12), fg="brown")
l15=Label(root, text="Reg L:", font=("Helvetica", 12), fg="brown")

#**********************************************************************************PLACING LABELS***********************************************************************

l1.place(x=460, y=20)
l2.place(x=857, y=35)
l3.place(x=889, y=63)
l4.place(x=889, y=90)
l5.place(x=855, y=114)
l6.place(x=882, y=138)
l7.place(x=882, y=162)
l8.place(x=1055, y=35)
l9.place(x=1080, y=63)
l10.place(x=1080, y=90)
l11.place(x=1080, y=114)
l12.place(x=1080, y=138)
l13.place(x=1080, y=162)
l14.place(x=1080, y=186)
l15.place(x=1080, y=210)

#**********************************************************************************VARIABLE LABLES**************************************************************************
var1=StringVar()
var1.set('0')
e1=Label(root, font=("calibri",11), fg="brown", textvariable=var1)
var2=StringVar()
var2.set('0')
e2=Label(root, font=("calibri",11), fg="brown", textvariable=var2)
var3=StringVar()
var3.set('0')
e3=Label(root, font=("calibri",11), fg="brown", textvariable=var3)
var4=StringVar()
var4.set('0')
e4=Label(root, font=("calibri",11), fg="brown", textvariable=var4)
var5=StringVar()
var5.set('0')
e5=Label(root, font=("calibri",11), fg="brown", textvariable=var5)
var6=StringVar()
var6.set('0')
e6=Label(root, font=("calibri",11), fg="brown", textvariable=var6)
var7=StringVar()
var7.set('0')
e7=Label(root, font=("calibri",11), fg="brown", textvariable=var7)
var8=StringVar()
var8.set('0')
e8=Label(root, font=("calibri",11), fg="brown", textvariable=var8)
var9=StringVar()
var9.set('0')
e9=Label(root, font=("calibri",11), fg="brown", textvariable=var9)
var10=StringVar()
var10.set('0')
e10=Label(root, font=("calibri",11), fg="brown", textvariable=var10)
var11=StringVar()
var11.set('0')
e11=Label(root, font=("calibri",11), fg="brown", textvariable=var11)
var12=StringVar()
var12.set('0')
e12=Label(root, font=("calibri",11), fg="brown", textvariable=var12)

#********************************************************************************PLACING VARIABLE LABLES********************************************************************

e1.place(x=945, y=63)
e2.place(x=945, y=90)
e3.place(x=945, y=114)
e4.place(x=945, y=138)
e5.place(x=945,y=162)
e6.place(x=1155, y=63)
e7.place(x=1155, y=90)
e8.place(x=1155, y=114)
e9.place(x=1155, y=138)
e10.place(x=1155, y=162)
e11.place(x=1155, y=186)
e12.place(x=1155, y=210)

txtarea=Text(width=45, height=30, font=("calibri",12), fg="brown", relief=GROOVE, borderwidth=4)                        #textarea for code
txtarea.place(x=420, y=50)
txtarea.focus()

txtarea1=Text(width=50, height=16, font=("calibri",12), fg="brown", relief=GROOVE, borderwidth=4)                       #txtarea1 is for errors
txtarea1.place(x=820, y=350)
l20=Label(text="ERRORS", font=("Helvetica", 16))
l20.place(x=970, y=320)
def err():
    a=''
    for i in register.error.keys():
        a+="Line{%s}='{%s}'\n"%(str(i),register.error[i])
    txtarea1.insert(1.0,a)

def execute():
    text=txtarea.get('1.0','end')
    with open("code.txt","w") as f:
        f.writelines(text)
    e13.delete(0,END)
    e14.delete(0,END)
    txtarea1.delete(1.0,END)
    set_()
    register.flag={'Z':0,'CY':0,'P':0,'AC':0,'S':0}
    main.verymain()
    err()
    # txtarea1.insert(1.0,register.error)
    register.error={}
    var1.set(register.flag['S'])
    var2.set(register.flag['Z'])
    var3.set(register.flag['AC'])
    var4.set(register.flag['P'])
    var5.set(register.flag['CY'])
    var6.set(hex(register.A.value).upper()[2:])
    var7.set(hex(register.B.value).upper()[2:])
    var8.set(hex(register.C.value).upper()[2:])
    var9.set(hex(register.D.value).upper()[2:])
    var10.set(hex(register.E.value).upper()[2:])
    var11.set(hex(register.H.value).upper()[2:])
    var12.set(hex(register.L.value).upper()[2:])
    register.cclear()
    #register.show()
    

def add_address():
    a=e13.get()
    b=e14.get()
    z=0
    if a=='' or b=='':
        z=2
    for i in a:
        if i.lower() not in {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
            z=1
    for i in b:
        if i.lower() not in {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
            z=1
    if z==0:
        if int(a,16)<65536 and int(b,16)<65536:
            register.data[int(a,16)]=int(b,16)
            e13.delete(0,'end')
            e13.insert(0,hex(int(a,16)+1)[2:])
            e14.delete(0,'end')
            e30.delete(0,'end')
        else:
            e30.delete(0,'end')
            e30.insert(0,'16 bit address and data')
    elif z==1:
        e30.delete(0,'end')
        e30.insert(0,'hexadecimal value')
    else:
        e30.delete(0,'end')
        e30.insert(0,'Enter in both column')
    print(register.data)
    

def go():
        z=0
        a=e13.get()
        for i in a:
            if i.lower() not in {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
                z=1
        if z==0:
            if int(a,16)<65536:
                e14.delete(0,'end')
                if int(a,16) in register.data.keys():
                    e14.insert(0,hex(register.data[int(a,16)])[2:])
                else:
                    e14.delete(0,'end')
                    e14.insert(0,0)   
            else:
                e30.delete(0,'end')
                e30.insert(0,"16 bit address")
        else:
            e30.delete(0,'end')
            e30.insert(0,'hexadecimal value')

frame3 = Frame(root, width=340, height=160, bd=3, relief="groove")                                   #Memory Segment Frame
frame3.place(x=20, y=180)
            
l18=Label(root, text="Memory Segment", font=("Helvetica", 16))
l18.place(x=28, y=165)
l16=Label(root, text="Address:", font=("Helvetica", 14), fg="brown")
l16.place(x=70, y=210)
e13=Entry(root, font=("calibri",11), fg="brown")
e13.place(x=40, y=240)
e13.focus()
l17=Label(root, text="Data:", font=("Helvetica", 14), fg="brown")
l17.place(x=250, y=210)
e14=Entry(root, font=("calibri",11), fg="brown")
e14.place(x=200, y=240)

frame4 = Frame(root, width=340, height=160, bd=3, relief="groove")                                  #IO Segment Frame
frame4.place(x=20, y=480)

l25=Label(root, text="IO Segment", font=("Helvetica", 16))
l25.place(x=28, y=470)
l22=Label(root, text="Port Address", font=("Helvetica", 14), fg="brown")
l22.place(x=48, y=520)
e18=Entry(root, font=("calibri",11), fg="brown")
e18.place(x=40, y=550)
e18.focus()
l23=Label(root, text="Data", font=("Helvetica", 14), fg="brown")
l23.place(x=245, y=520)
e19=Entry(root, font=("calibri",11), fg="brown")
e19.place(x=200, y=550)

l17=Label(root, text="Enter Starting Address:", font=("Helvetica", 14), fg="brown")                  #sets starting address
l17.place(x=40, y=45)
e20=Entry(root, font=("calibri",11), fg="brown")                                                     
e20.place(x=70, y=75)
e20.insert(0,2000)

e30=Entry(root, font=("calibri",11), fg="brown", borderwidth=2)
e30.place(x=60, y=400)
def set_():
        parse.get_Counter(str(e20.get()))



def set_io():
    a=e18.get()
    b=e19.get()
    z=0
    if a=='' or b=='':
        z=2
    for i in a:
        if i.lower() not in {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
            z=1
    for i in b:
        if i.lower() not in {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
            z=1
    if z==0:
        if int(a,16)<256 and int(b,16)<256:
            register.io[int(a,16)]=int(b,16)
            e18.delete(0,'end')
            e19.delete(0,'end')
            e30.delete(0,'end')
        else:
            e30.delete(0,'end')
            e30.insert(0,'8 bit address and data')
    elif z==1:
        e30.delete(0,'end')
        e30.insert(0,'hexadecimal value')
    else:
        e30.delete(0,'end')
        e30.insert(0,'Enter in both column')
    print(register.io)

def show():
        z=0
        a=e18.get()
        for i in a:
            if i.lower() not in {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
                z=1
        if z==0:
            if int(a,16)<256:
                e19.delete(0,'end')
                if int(a,16) in register.io.keys():
                    e19.insert(0,hex(register.io[int(a,16)])[2:])
                else:
                    e19.delete(0,'end')
                    e19.insert(0,0)   
            else:
                e30.delete(0,'end')
                e30.insert(0,"8 bit port address")
        else:
            e30.delete(0,'end')
            e30.insert(0,'hexadecimal value')

b1=Button(text="COMPILE & RUN", command=execute, fg="brown", borderwidth=3)
b1.place(x=600, y=640)

b2=Button(text="ADD", command=add_address, fg="brown")
b2.place(x=250, y=280)
        
b3=Button(text="SHOW", command=go, fg="brown")
b3.place(x=85, y=280)

b4=Button(text="IN", command=set_io, fg="brown")
b4.place(x=260, y=590)

b5=Button(text="OUT", command=show, fg="brown")
b5.place(x=95, y=590)



#******************************************************************SUBROUTINE WINDOW************************************************************************************

def sub():
        root=Tk()
        root.after(1, lambda: root.focus_force())
        root.geometry("600x600+75+20")
        root.title("SUBROUTINE")
        l1=Label(root, text="Load me at:", font=("Helvetica", 14), fg="brown")
        l1.place(x=180,y=10)
        l1=Label(root, text="Enter Code Here:", font=("Helvetica", 16), fg="brown")
        l1.place(x=220,y=40)
        e1=Entry(root, font=("calibri",11), fg="brown")
        e1.place(x=290, y=10)
        txtarea2=Text(root,width=35, height=25, font=("calibri",12), fg="brown", relief=GROOVE, borderwidth=4)
        txtarea2.place(x=170, y=75)
        def set_sub():
                g=e1.get()
                store(g)
                text=txtarea2.get('1.0','end')
                with open("subroutine.txt","w") as f:
                        f.writelines(text)
                if 'subroutine add' not in register.error.keys() and 'subroutine' not in register.error.keys():
                    parse.get_subroutine()
                    print(register.data)
                    tkinter.messagebox.showinfo("SUCCESSFUL","Subroutine succesfuly added")
                else:
                    tkinter.messagebox.showinfo("UNSUCCESSFUL","CANNOT CREATE SUBROUTINE")
                root.destroy()
        b1=Button(root, text="SUBMIT", command=set_sub, fg="brown", borderwidth=3)
        b1.place(x=280, y=565)
        txtarea2.focus()
        
        root.mainloop()
 
def store(add):
    z=0
    if add=='':
        parse.sub_var=16384
        return
    for i in add:
        if i.lower() not in {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
            z=1
    if z==0:
        if int(add,16)<65536:
            parse.sub_var=int(add,16)
        else:
            register.error['subroutine add']="enter 16 bit address"
    else:
        register.error['subroutine']="enter valid address"

b8=Button(text="SUBROUTINE", command=sub, fg="brown", borderwidth=3)
b8.place(x=500, y=640)
root.mainloop()

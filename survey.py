import tkinter 
from tkinter import *
from math import *

root=tkinter.Tk()
root.title("Survey")
root.geometry("750x600")

frame=Frame(root,pady=170)
frame.pack(fill=BOTH,expand=YES)

northing1=0
northing2=0
easting1=0
easting2=0
bearing=0
distance=0
degrees=0
minutes=0
seconds=0
foresight=0
backsight=0
intersight=0
rlevel=0

northing1=tkinter.DoubleVar()
northing2=tkinter.DoubleVar()
easting1=tkinter.DoubleVar()
easting2=tkinter.DoubleVar()
degrees=tkinter.IntVar()
minutes=tkinter.IntVar()
seconds=tkinter.IntVar()
distance=tkinter.DoubleVar()
foresight=tkinter.DoubleVar()
backsight=tkinter.DoubleVar()
intersight=tkinter.DoubleVar()
rlevel=tkinter.DoubleVar()

def convertint(angle):
    value=float(angle)
    value1=int(value)
    return value1

def convert(angle):
    value=float(angle)
    value1=int(value)
    value2=value-value1
    value3=value2*60
    return value3

def traverse():
    for Widget in root.winfo_children():
        Widget.destroy()

    frame=Frame(root)
    frame.pack(fill=BOTH,expand=YES)
    toplabel=LabelFrame(frame,relief=GROOVE)
    trvlabel=Label(toplabel,text="TRAVERSING",font=("Courier New",14,'bold'))
    trvlabel.pack()
    toplabel.pack(fill=X)

    def rectopol():  
        for Widget in frame.winfo_children():
            Widget.destroy()

        toplabel=LabelFrame(frame,relief=GROOVE)
        trvlabel=Label(toplabel,text="TRAVERSING",font=("Courier New",14,'bold'))
        trvlabel.pack()
        toplabel.pack(fill=X)
        
        midframe=Frame(frame,bd=1,relief=GROOVE,pady=50)
        midframe.pack(fill=BOTH,expand=YES)

        datainput=Frame(midframe)
        datainput.pack()
        
        stationlabel=Label(datainput,text="Theodolite station::",font=("Courier New",14,'bold')).grid(row=0,column=0,padx=60,columnspan=2)
        N1label=Label(datainput,text="N1",font=("Courier New",13,'bold')).grid(row=1,column=0)
        E1label=Label(datainput,text="E1",font=("Courier New",13,'bold')).grid(row=1,column=1)

        N1=Entry(datainput,width=37,relief=RIDGE,bd=1.5,textvariable=northing1).grid(row=2,column=0)
        E1=Entry(datainput,width=37,relief=RIDGE,bd=1.5,textvariable=easting1).grid(row=2,column=1,padx=2)

        orstationlabel=Label(datainput,text="Oriented to::",font=("Courier New",14,'bold')).grid(row=3,column=0,columnspan=2)
        N2label=Label(datainput,text="N2",font=("Courier New",13,'bold')).grid(row=4,column=0)
        E2label=Label(datainput,text="E2",font=("Courier New",13,'bold')).grid(row=4,column=1)

        N2=Entry(datainput,width=37,relief=RIDGE,bd=1.5,textvariable=northing2).grid(row=5,column=0)
        E2=Entry(datainput,width=37,relief=RIDGE,bd=1.5,textvariable=easting2).grid(row=5,column=1,padx=2)
        def compute():
            global northing1
            global northing2
            global easting1
            global easting2
            Northing1=float(northing1.get())
            Easting1=float(easting1.get())
            Northing2=float(northing2.get())
            Easting2=float(easting2.get())
            N=Northing2-Northing1
            E=Easting2-Easting1

            distance=sqrt((pow(N,2)+pow(E,2)))
            try:
                anglerad=atan(E/N)
                angledeg=(anglerad*360)/(2*3.141592654)
            except ZeroDivisionError:
                pass
            if E>0 and N>0:
                quadrant='First'
                angledeg=angledeg
                angle=convertint(angledeg)
                minutes=convert(angledeg)
                second=convert(minutes)
            elif E>0 and N<0:
                quadrant='Second'
                angledeg=180-angledeg
                angle=convertint(angledeg)
                minutes=convert(angledeg)
                second=convert(minutes)
            elif E<0 and N<0:
                quadrant='Third'
                angledeg+=180
                angle=convertint(angledeg)
                minutes=convert(angledeg)
                second=convert(minutes)
            elif E<0 and N>0:
                quadrant='Fourth'
                angledeg+=360
                angle=convertint(angledeg)
                minutes=convert(angledeg)
                second=convert(minutes)
            elif E>0 and N==0:
                quadrant='First'
                angledeg=90
                angle=convertint(angledeg)
                minutes=convert(angledeg)
                second=convert(minutes)
            elif E==0 and N<0:
                quadrant='Second'
                angledeg=180
                angle=convertint(angledeg)
                minutes=convert(angledeg)
                second=convert(minutes)
            elif E<0 and N==0:
                quadrant='Third'
                angledeg=270
                angle=convertint(angledeg)
                minutes=convert(angledeg)
                second=convert(minutes)
            elif E==0 and N>0:
                quadrant='Fourth'
                angledeg=0
                angle=convertint(angledeg)
                minutes=convert(angledeg)
                second=convert(minutes)
            resultd=Entry(datainput,font=("Courier New",15,'bold'),width=50)
            resultd.insert(0,"Distance:: "+str("%3.2F"%distance+" metres"))
            resulta=Entry(datainput,font=("Courier New",15,'bold'),width=50)
            resulta.insert(0,"Bearing:: %3.0f"%angle+"deg %2.0f"%minutes+"min %2.0f"%second+"sec")
            resultd.grid(row=7,column=0,columnspan=2)
            resulta.grid(row=8,column=0,columnspan=2,pady=5)
            btn=Button(datainput,text="Done",font=("Courier New",14,'bold'),command=rectopol,width=37)
            btn.grid(row=9,column=0,columnspan=2)
            
        

        btnsubmit=Button(datainput,width=15,text="COMPUTE",font=("Courier New",14,'bold'),command=compute).grid(row=6,column=0,columnspan=2,pady=5)

        dataoutput=Frame(midframe,pady=10)
        dataoutput.pack()
    #The portion that computes the polar computations
    def poltorec():
        for Widget in frame.winfo_children():
            Widget.destroy()

        toplabel=LabelFrame(frame,relief=GROOVE)
        trvlabel=Label(toplabel,text="TRAVERSING",font=("Courier New",14,'bold'))
        trvlabel.pack()
        toplabel.pack(fill=X)
        
        midframe=Frame(frame,bd=1,relief=GROOVE,pady=50)
        midframe.pack(fill=BOTH,expand=YES)
        datainput=Frame(midframe)
        datainput.pack()

        dinput1=Frame(datainput)
        dinput1.pack(expand=YES)
        stnlabel=Label(dinput1,text="Known Coordinates",font=("Courier New",14,'bold')).grid(row=0,column=0,columnspan=3)
        Nlabel=Label(dinput1,text="N",font=("Courier New",14,'bold')).grid(row=1,column=0)
        Elabel=Label(dinput1,text="E",font=("Courier New",14,'bold')).grid(row=1,column=1)

        Nentry=Entry(dinput1,textvariable=northing1,font=("Courier New",14),width=23).grid(row=2,column=0)
        Eentry=Entry(dinput1,textvariable=easting1,font=("Courier New",14),width=23).grid(row=2,column=1,padx=3)
        
        dinput2=Frame(datainput)
        dinput2.pack(expand=YES,pady=15)
        Alabel=Label(dinput2,text="Bearing",font=("Courier New",14,'bold')).grid(row=1,column=0,columnspan=3)

        deglbl=Label(dinput2,text="deg",font=("Courier New",13,'bold')).grid(row=2,column=0)
        minlbl=Label(dinput2,text="min",font=("Courier New",13,'bold')).grid(row=2,column=1)
        seclbl=Label(dinput2,text="sec",font=("Courier New",13,'bold')).grid(row=2,column=2)

        Degentry=Entry(dinput2,textvariable=degrees,font=("Courier New",13),width=17).grid(row=3,column=0)
        minentry=Entry(dinput2,textvariable=minutes,font=("Courier New",13),width=17).grid(row=3,column=1,padx=2)
        secentry=Entry(dinput2,textvariable=seconds,font=("Courier New",13),width=17).grid(row=3,column=2)
        
        dinput3=Frame(datainput)
        dinput3.pack(pady=10)

        dstlbl=Label(dinput3,text="Distance:",font=("Courier New",14,'bold')).grid(row=0,column=0)
        dstentry=Entry(dinput3,textvariable=distance,font=("Courier New",13),width=43).grid(row=0,column=1)
        def compute():
            global degrees
            global minutes
            global seconds
            global distance
            global northing1
            global easting1

            # convert degrees, minutes and seconds to a float angle
            def convert(a,b,c):
                value1=float(c/60)
                value2=float(value1+b)
                value3=float(value2/60)
                value4=float(value3+a)
                return value4

            Northing=float(northing1.get())
            Easting=float(easting1.get())
            deg=int(degrees.get())
            mins=int(minutes.get())
            sec=int(seconds.get())
            distance=float(distance.get())
            
            angle=convert(deg,mins,sec)
            angle=(angle*3.141592654)/180
            N=distance*cos(angle)
            northing=Northing+N
            E=distance*sin(angle)
            easting=Easting+E

            rlabel=Label(dinput3,text="New coordinates",font=("Courier New",14,'bold')).grid(row=3,column=0,columnspan=2)
            resultc=Entry(dinput3,font=("Courier New",14,'bold'),width=25)
            resultc.insert(0,"(%.3f"%northing+",%.3f"%easting+")")
            resultc.grid(row=4,column=0,columnspan=2)
            btn=Button(dinput3,text="Done",font=("Courier New",14,'bold'),command=poltorec,width=37)
            btn.grid(row=5,column=0,columnspan=2)

        btncompute=Button(dinput3,width=15,text="COMPUTE",font=("Courier New",14,'bold'),command=compute).grid(row=2,column=0,columnspan=2)


    midframe=Frame(frame,bd=1,relief=GROOVE,pady=130)
    midframe.pack(fill=BOTH,expand=YES)
    
    recconv=Button(midframe,text="POL",font=("Courier New",15,'bold'),width=17,command=rectopol)
    recconv.pack()
    polconv=Button(midframe,text="REC",font=("Courier New",15,'bold'),width=17,command=poltorec)
    polconv.pack(pady=10)
        
def level():
    for Widget in root.winfo_children():
        Widget.destroy()
    frame=Frame(root)
    frame.pack(fill=BOTH,expand=YES)
    def HOC():
        global backsight
        global intersight
        global foresight
        global rlevel
        for Widget in midframe.winfo_children():
            Widget.destroy()
    
    def RAF():
        global backsight
        global intersight
        global foresight
        global rlevel
        for Widget in midframe.winfo_children():
            Widget.destroy()
    topframe=LabelFrame(frame)
    topframe.pack(fill=X)
    toplabel=Label(topframe,text="LEVELLING",font=("Courier New",15,'bold'))
    toplabel.pack()

    midframe=Frame(frame)
    midframe.pack(expand=YES,ipady=50)
    HC=Button(midframe,text="HEIGHT OF COLLIMATION",font=("Courier New",13,'bold'),width=37,command=HOC).pack()
    RF=Button(midframe,text="RISE AND FALL", font=("Courier New",13,'bold'),width=37,command=RAF).pack(pady=5)


btntraverse=Button(frame,text="Traversing",width=20,font=("Courier New",15,'bold'),command=traverse)
btntraverse.pack(expand=NO)
btnlevel=Button(frame,text="Leveling",width=20,font=("Courier New",15,'bold'),command=level)
btnlevel.pack(expand=NO,pady=10)

root.mainloop()
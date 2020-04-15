from tkinter import *
import time
l=[74, 79, 72, 78, 81, 72, 81, 89, 84, 74, 99, 90, 77, 94, 83, 94, 87, 78, 98, 81, 92, 83, 91, 92, 74, 92, 76, 72, 90, 83, 91, 91, 75, 86, 70, 89, 96, 89, 72, 70, 87, 77, 84, 83, 81, 72, 80, 71, 97, 91, 86, 89, 92, 86, 87, 89, 82, 86, 97, 78, 90, 82, 84, 97, 95, 77, 72, 86, 85, 74, 75, 83, 71, 88, 96, 99, 88, 87, 75, 96, 93, 78, 80, 93, 75, 75, 94, 73, 88, 70, 85, 91, 94, 92, 85, 72, 72, 89, 79, 87]

ctr=0
def TrafficLights():
    def red():
        global ctr,l
        canvas.itemconfig(r, fill="red")
        canvas.itemconfig(g, fill="white")
        l1=Label(obj,text="Decibel: {}".format(l[ctr])).grid(row=1,column=0)
        ctr=ctr+1
        if(l[ctr]>80):
            obj.after(1000, red)
        else:
            obj.after(1000, green)
    def green():
        global ctr,l
        canvas.itemconfig(r, fill="white")
        canvas.itemconfig(g, fill="green")
        l1=Label(obj,text="Decibel: {}".format(l[ctr])).grid(row=1,column=0)
        ctr=ctr+1
        if(l[ctr]>80):
            obj.after(1000, red)
        else:
            obj.after(1000, green)
    global ctr,l
    if(l[ctr]>80):
        x,y,z='red','white','white'
    else:
        x,y,z='white','white','green'
    obj=Tk()
    obj.title('Traffic Lights')
    l1=Label(obj,text="Decibel: {}".format(l[ctr])).grid(row=1,column=0)
    canvas=Canvas(obj, width = 300, height = 400, bg = "black")
    canvas.grid(row=0,column=0)
    canvas.create_rectangle(100, 50, 200, 350)
    r=canvas.create_oval(100, 50, 200, 150, fill=x)
    canvas.create_oval(100, 150, 200, 250, fill=y)
    g=canvas.create_oval(100, 250, 200, 350, fill=z)
    ctr=ctr+1
    if(l[ctr]>80):
        obj.after(1000, red)
    else:
        obj.after(1000, green)
    obj.mainloop()
        

def main():
    TrafficLights()

main()

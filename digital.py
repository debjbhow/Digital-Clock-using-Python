from tkinter import*
import time
root = Tk()
root.title("Digital Clock")
root.geometry("1350x700+0+0")
root.config(bg= "#081923")

def clock():
    h= str(time.strftime("%H"))
    m= str(time.strftime("%M"))
    s= str(time.strftime("%S"))
    # print(h,m,s)

    if int(h)>= 12 and int(m)>0:
        lbl_noon1.config(text= "PM")

    if int(h)> 12:
        h = str((int(h)-12))


    lbl_hr1.config(text=h)
    lbl_min1.config(text=m)
    lbl_sec1.config(text=s)

    lbl_hr1.after(200, clock)

lbl_hr1= Label(root, text="12", font=("times new roman", 50, "bold"), bg="#087587", fg="white")
lbl_hr1.place(x=350, y= 200, width= 150, height= 150)

lbl_hr2= Label(root, text="HOUR", font=("times new roman", 20, "bold"), bg="#087587", fg="white")
lbl_hr2.place(x=350, y= 360, width= 150, height= 50)

lbl_min1= Label(root, text="12", font=("times new roman", 50, "bold"), bg="#ADD8E6", fg="white")
lbl_min1.place(x=520, y= 200, width= 150, height= 150)

lbl_min2= Label(root, text="MINUTE", font=("times new roman", 20, "bold"), bg="#ADD8E6", fg="white")
lbl_min2.place(x=520, y= 360, width= 150, height= 50)

lbl_sec1= Label(root, text="12", font=("times new roman", 50, "bold"), bg="#FFFF00", fg="white")
lbl_sec1.place(x=690, y= 200, width= 150, height= 150)

lbl_sec2= Label(root, text="SECOND", font=("times new roman", 20, "bold"), bg="#FFFF00", fg="white")
lbl_sec2.place(x=690, y= 360, width= 150, height= 50)

lbl_noon1= Label(root, text= "AM", font=("times new roman", 50, "bold"), bg="#DF002A", fg="white")
lbl_noon1.place(x=860, y= 200, width= 150, height= 150)

lbl_noon2= Label(root, text= "NOON", font=("times new roman", 20, "bold"), bg="#DF002A", fg="white")
lbl_noon2.place(x=860, y= 360, width= 150, height= 50)

clock()
root.mainloop()
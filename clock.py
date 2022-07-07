from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.config(bg="grey22")
root.geometry("1000x1000")
clock_img=ImageTk.PhotoImage(Image.open("clock.jpg"))

indlbl=Label(root,text="IST")
indlbl.place(relx=0.3,rely=0.6,anchor=CENTER)

uslbl=Label(root,text="CST")
uslbl.place(relx=0.7,rely=0.6,anchor=CENTER)

auslbl=Label(root,text="ACT")
auslbl.place(relx=0.425,rely=0.6,anchor=CENTER)

japlbl=Label(root,text="JCST")
japlbl.place(relx=0.575,rely=0.6,anchor=CENTER)

ist= Label(root)
ist.place(relx=0.3,rely=0.7,anchor=CENTER)

cst= Label(root)
cst.place(relx=0.7,rely=0.7,anchor=CENTER)

jst= Label(root)
jst.place(relx=0.575,rely=0.7,anchor=CENTER)

ast= Label(root)
ast.place(relx=0.425,rely=0.7,anchor=CENTER)



class INDIA():
    def times(self):
        home=pytz.timezone("Asia/Kolkata")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        ist["text"]="India :"+current_time+"hrs"
        ist.after(200,self.times)
    
    
obj1=INDIA()
btn1= Button(root,text="Show Time",command=obj1.times)
btn1.place(relx=0.3,rely=0.2,anchor=CENTER)

class USA():
    def times(self):
        home=pytz.timezone("US/Central")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        cst["text"]="USA :"+current_time+"hrs"
        cst.after(200,self.times)
    
    
obj2=USA()
btn2= Button(root,text="Show Time",command=obj2.times)
btn2.place(relx=0.7,rely=0.2,anchor=CENTER)

class Japan():
    def times(self):
        home=pytz.timezone("Japan")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        jst["text"]="Japan :"+current_time+"hrs"
        jst.after(200,self.times)
    
    
obj3=Japan()
btn3= Button(root,text="Show Time",command=obj3.times)
btn3.place(relx=0.575,rely=0.2,anchor=CENTER)

class Australia():
    def times(self):
        home=pytz.timezone("Australia/ACT")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        ast["text"]="Australia :"+current_time+"hrs"
        ast.after(200,self.times)
    
    
obj4=Australia()
btn4= Button(root,text="Show Time",command=obj4.times)
btn4.place(relx=0.425,rely=0.2,anchor=CENTER)
root.mainloop()
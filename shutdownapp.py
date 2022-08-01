# from logging import shutdown
# from math import radians
from tkinter import *
import os



def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")         
def logout():
    os.system("logout -1")  
def shutdown():
    os.system("shutdown /r /t 1")  


st = Tk()


st.title("Shutdown App")
# st.geometry("500X500")
st.config(bg ="blue")


r_button = Button(st,text= "Restart",font= ("Time New Roman", 30,
            "bold"),relief=RAISED,cursor = "plus",command=restart)
r_button.place(x=600, y=60, width=150)

rt_button = Button(st,text= "Restart Time",font= ("Time New Roman", 
             15, "bold"),relief=RAISED,cursor = "plus",command= restart_time)
rt_button.place(x=600, y=170, width=150)

lg_button = Button(st,text= "Log-Out",font= ("Time New Roman", 20,
             "bold"),relief=RAISED,cursor = "plus",command= logout)
lg_button.place(x=600, y=250, width=150)

st_button = Button(st,text= "ShutDown",font= ("Time New Roman", 20, 
             "bold"),relief=RAISED,cursor = "plus", command= shutdown)
st_button.place(x=600, y=350, width=150)







st.mainloop()




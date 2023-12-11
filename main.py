import tkinter
import keyboard as key
import pyautogui as pag
from tkinter import *
position = ""
def find_location():
    try:
        while True:
            if key.is_pressed("space"):
                position = pag.position()
                textbox = tkinter.Label(master=app, text=str(position),bg="white")
                textbox.place(x=50,y=28)
                break
            else:

                continue

    except:
        print("unable to display the mouse position")

app = Tk()
app.geometry("200x100")
app.title("Mouse Location")


find_btn = tkinter.Button(master=app,text="Find Mouse Location.",command=find_location)
find_btn.place(x=50,y=0)
lbl = tkinter.Label(master=app,text="Press pacebar to record location.",bg='red')
lbl.place(x=22,y=50)
app.mainloop()






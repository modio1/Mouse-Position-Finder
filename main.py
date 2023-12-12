import tkinter
import keyboard as key
import pyautogui

import pyautogui as pag
from PIL import *
from tkinter import *
position = ""
def find_location():
    try:
        while True:
            if key.is_pressed("space"):
                position = pag.position()
                x,y = pag.position()
                color = get_pixel_color_pyautogui(x,y)
                rgb_values = color
                color_string = "#{:02X}{:02X}{:02X}".format(*rgb_values)
                textbox = tkinter.Label(master=app, text=str(position),bg="white")
                textbox.place(x=50,y=28)
                colorbox = tkinter.Label(master=app, text="", bg="white")
                colorbox.place(x=70, y=70)
                colorbox = tkinter.Label(master=app,text=str(color),bg=color_string)
                colorbox.place(x=70,y=70)

                break
            else:

                continue

    except:
        print("unable to display the mouse position")
def get_pixel_color_pyautogui(x, y):
    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Get the color of the pixel at coordinates (x, y)
    pixel_color = screenshot.getpixel((x, y))

    return pixel_color

app = Tk()
app.geometry("200x100")
app.title("Mouse Location")


find_btn = tkinter.Button(master=app,text="Find Mouse Location.",command=find_location)
find_btn.place(x=50,y=0)
lbl = tkinter.Label(master=app,text="Press pacebar to record location.",bg='red')
lbl.place(x=22,y=50)
app.mainloop()






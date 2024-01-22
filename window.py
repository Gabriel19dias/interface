from tkinter import *
import pyautogui as py 
import selenium as sl 




   
   
def btn_clicked():
    py.press('win')


window = Tk()

window.geometry("478x293")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 293,
    width = 484,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    230.0, 127.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button (
    #image = img0,
    borderwidth = 0,
    text= 'iniciar',
    background='gray',
    fg= 'white',
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 152, y = 168,
    width = 156,
    height = 17)

window.resizable(False, False)
window.mainloop()

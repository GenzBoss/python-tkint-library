import tkinter as tk
from tkinter import *
wind=Tk()

btn = Button()
btn.pack()
btn["text"]="Hello everyone!"

def click():
    print("you just clicked me!")
btn["command"]= click

wind.mainloop()



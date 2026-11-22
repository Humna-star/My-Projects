from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x200")

def msg():
    messagebox.askokcancel("Answer in Yes or Cancel! ", "Do you complete your homework and other tasks?")

button = Button(root, text="Routine Checker", command=msg )
button.place(x=150, y=80)

root.mainloop()
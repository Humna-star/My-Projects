from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x200")

def msg():
    messagebox.showwarning("Alert! Virus Detected", "A virus has been detected on your system.")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=175, y=80)

root.mainloop()
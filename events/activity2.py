from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def message():
    messagebox.showwarning("Alert", "Stop! Virus found")

button = Button(root, text = "Scan for virus", command = message)
button.place(x = 40, y = 80)

root.mainloop()
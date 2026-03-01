from tkinter import *

window = Tk()
window.title('Event Handler')
window.geometry("100x100")

def handle_keypress(event):
    print(event.char)

window.bind("<key>", handle_keypress)

def handle_click(event):
    print("\nThe Button Was Clicked!!")

button = Button(text = "Click Me!")
button.pack()

button.bind("<button-1>", handle_click)

window.mainloop()

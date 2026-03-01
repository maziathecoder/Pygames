from tkinter import *

def convert():
    inches = float(entry.get())
    centimeters = inches * 2.54
    
    result = f"{inches} inches is equal to {centimeters:.2f} centimeters."
    textbox.insert(END, result)

root = Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x400")

label = Label(root, text="Enter length in inches:", font=("Arial", 12))
label.pack(pady=20)

entry = Entry(root, font=("Arial", 12))
entry.pack(pady=10)

button = Button(root, text="Convert", command=convert)
button.pack(pady=10)

textbox = Text(root, height=5)
textbox.pack(pady=20)

root.mainloop()
from tkinter import *

def check_strength():
    password = entry_password.get()
    length = len(password)

    if length <= 5:
        result_label.config(text="Weak Password", fg="red")
    elif length >= 6 and length <= 8:
        result_label.config(text="Medium Password", fg="yellow")
    elif length > 8 and length <= 12:
        result_label.config(text="Strong Password", fg="light green")
    else:
        result_label.config(text="Very Strong Password", fg="dark green")

root = Tk()
root.title("Password Strength Checker App")
root.geometry("400x400")

title_label = Label(root, text="Password Strength Checker", font=("Arial", 16))
title_label.pack(pady=20)

label_password = Label(root, text="Enter Password:")
label_password.pack()

entry_password = Entry(root, show="*", width=25)
entry_password.pack(pady=10)

check_button = Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
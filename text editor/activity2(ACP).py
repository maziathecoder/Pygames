import tkinter as tk
from tkinter import messagebox

# Function to calculate interests
def calculate_interest():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())
        simple_interest = (principal * rate * time) / 100
        compound_interest = principal * ((1 + rate/100) ** time) - principal

        label_si_result.config(text=f"Simple Interest: {simple_interest:.2f}")
        label_ci_result.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

heading = tk.Label(root, text="Interest Calculator", font=("Arial", 16, "bold"), bg="#f2f2f2")
heading.pack(pady=10)

description = tk.Label(
    root,
    text="Enter Principal, Time (years) and Rate (%)\nto calculate Simple and Compound Interest",
    bg="#f2f2f2"
)
description.pack(pady=5)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=15)

label_principal = tk.Label(frame, text="Principal:", bg="#f2f2f2")
label_principal.grid(row=0, column=0, padx=10, pady=5)

entry_principal = tk.Entry(frame)
entry_principal.grid(row=0, column=1, padx=10, pady=5)

label_time = tk.Label(frame, text="Time (years):", bg="#f2f2f2")
label_time.grid(row=1, column=0, padx=10, pady=5)

entry_time = tk.Entry(frame)
entry_time.grid(row=1, column=1, padx=10, pady=5)

label_rate = tk.Label(frame, text="Rate (%):", bg="#f2f2f2")
label_rate.grid(row=2, column=0, padx=10, pady=5)

entry_rate = tk.Entry(frame)
entry_rate.grid(row=2, column=1, padx=10, pady=5)

calculate_btn = tk.Button(root, text="Calculate Interest", command=calculate_interest, bg="#4CAF50", fg="white")
calculate_btn.pack(pady=10)

label_si_result = tk.Label(root, text="Simple Interest: ", font=("Arial", 11), bg="#f2f2f2")
label_si_result.pack(pady=5)

label_ci_result = tk.Label(root, text="Compound Interest: ", font=("Arial", 11), bg="#f2f2f2")
label_ci_result.pack(pady=5)

root.mainloop()
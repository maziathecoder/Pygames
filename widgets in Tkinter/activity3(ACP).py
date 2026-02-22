import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"Product: {product}")
    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter valid numbers!")

window = tk.Tk()
window.title("Get Start with Widgets")
window.geometry("400x300")
window.configure(bg="black")

desc_label = tk.Label(
    window,
    text="This application multiplies two numbers.",
    bg="black",
    fg="green",
    font=("Arial", 12)
)
desc_label.pack(pady=10)

label1 = tk.Label(window, text="Enter First Number:", bg="black", fg="green")
label1.pack()

entry1 = tk.Entry(window, bg="green", fg="black")
entry1.pack(pady=5)

label2 = tk.Label(window, text="Enter Second Number:", bg="black", fg="green")
label2.pack()

entry2 = tk.Entry(window, bg="green", fg="black")
entry2.pack(pady=5)

calc_button = tk.Button(
    window,
    text="Calculate Product",
    bg="green",
    fg="black",
    command=calculate_product
)
calc_button.pack(pady=10)

result_box = tk.Text(window, height=2, width=30, bg="black", fg="green")
result_box.pack(pady=5)

window.mainloop()
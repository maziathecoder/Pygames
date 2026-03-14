import tkinter as tk
import random

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

choices = ["Rock", "Paper", "Scissors"]

label = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16))
label.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"

    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"Your Choice: {user_choice}\nComputer Choice: {computer_choice}\nResult: {result}"
    )

rock_button = tk.Button(root, text="Rock", width=12, command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=12, command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=12, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

root.mainloop()
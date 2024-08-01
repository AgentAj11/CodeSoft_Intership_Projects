import tkinter as tk
from tkinter import messagebox
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Initialize scores
user_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    global user_score, computer_score
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    return result

def play_game(user_choice):
    """Play a round of Rock-Paper-Scissors."""
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    label_user_choice.config(text=f"Your Choice: {user_choice}")
    label_computer_choice.config(text=f"Computer's Choice: {computer_choice}")
    label_result.config(text=result)
    label_score.config(text=f"Score - You: {user_score} Computer: {computer_score}")

def reset_game():
    """Reset the game scores."""
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_user_choice.config(text="Your Choice: ")
    label_computer_choice.config(text="Computer's Choice: ")
    label_result.config(text="")
    label_score.config(text=f"Score - You: {user_score} Computer: {computer_score}")

# Initialize main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# User instructions
label_instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label_instructions.pack(pady=10)

# Buttons for user choices
frame_choices = tk.Frame(root)
frame_choices.pack(pady=10)

btn_rock = tk.Button(frame_choices, text="Rock", command=lambda: play_game("Rock"))
btn_rock.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(frame_choices, text="Paper", command=lambda: play_game("Paper"))
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = tk.Button(frame_choices, text="Scissors", command=lambda: play_game("Scissors"))
btn_scissors.grid(row=0, column=2, padx=5)

# Display user and computer choices
label_user_choice = tk.Label(root, text="Your Choice: ")
label_user_choice.pack(pady=5)

label_computer_choice = tk.Label(root, text="Computer's Choice: ")
label_computer_choice.pack(pady=5)

# Display result
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Display score
label_score = tk.Label(root, text=f"Score - You: {user_score} Computer: {computer_score}")
label_score.pack(pady=10)

# Reset game button
btn_reset = tk.Button(root, text="Reset Game", command=reset_game)
btn_reset.pack(pady=10)

# Start the GUI event loop
root.mainloop()

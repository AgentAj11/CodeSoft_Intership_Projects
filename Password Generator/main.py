import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """Generate a random password based on the specified criteria."""
    length = entry_length.get()
    
    if not length.isdigit() or int(length) < 1:
        messagebox.showerror("Input Error", "Please enter a valid length (positive integer)")
        return
    
    length = int(length)
    
    characters = ""
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_lowercase.get():
        characters += string.ascii_lowercase
    if var_numbers.get():
        characters += string.digits
    if var_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Input Error", "Please select at least one character type")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

# Initialize main window
root = tk.Tk()
root.title("Password Generator")

# Input for password length
frame_length = tk.Frame(root)
frame_length.pack(pady=10)

label_length = tk.Label(frame_length, text="Password Length:")
label_length.grid(row=0, column=0, padx=5)
entry_length = tk.Entry(frame_length)
entry_length.grid(row=0, column=1, padx=5)

# Checkbuttons for password complexity
frame_options = tk.Frame(root)
frame_options.pack(pady=10)

var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_special = tk.BooleanVar()

check_uppercase = tk.Checkbutton(frame_options, text="Include Uppercase", variable=var_uppercase)
check_uppercase.grid(row=0, column=0, padx=5, pady=2)
check_lowercase = tk.Checkbutton(frame_options, text="Include Lowercase", variable=var_lowercase)
check_lowercase.grid(row=1, column=0, padx=5, pady=2)
check_numbers = tk.Checkbutton(frame_options, text="Include Numbers", variable=var_numbers)
check_numbers.grid(row=0, column=1, padx=5, pady=2)
check_special = tk.Checkbutton(frame_options, text="Include Special Characters", variable=var_special)
check_special.grid(row=1, column=1, padx=5, pady=2)

# Generate password button
frame_generate = tk.Frame(root)
frame_generate.pack(pady=10)

btn_generate = tk.Button(frame_generate, text="Generate Password", command=generate_password)
btn_generate.grid(row=0, column=0, padx=5)

# Display generated password
frame_password = tk.Frame(root)
frame_password.pack(pady=10)

label_password = tk.Label(frame_password, text="Generated Password:")
label_password.grid(row=0, column=0, padx=5)
entry_password = tk.Entry(frame_password, width=50)
entry_password.grid(row=0, column=1, padx=5)

# Start the GUI event loop
root.mainloop()

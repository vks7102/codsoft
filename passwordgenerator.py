import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def on_generate():
    try:
        # Get the desired length from the input field
        length = int(length_entry.get())
        if length < 6:
            messagebox.showwarning("Invalid Length", "Password length should be at least 6 characters.")
            return
        
        # Generate the password
        password = generate_password(length)
        password_entry.delete(0, tk.END)  # Clear the entry field
        password_entry.insert(0, password)  # Insert the generated password

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the labels and input fields
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

# Run the GUI application
root.mainloop()

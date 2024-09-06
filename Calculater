from tkinter import *

# Global variable to store the expression
expression = ""

# Function to update expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" Error ")
        expression = ""

# Function to clear the contents of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Create the main window
gui = Tk()
gui.title("Simple Calculator")
gui.configure(background="light blue")
gui.geometry("300x400")

# StringVar to store the expression
equation = StringVar()

# Entry widget for displaying the expression
expression_field = Entry(gui, textvariable=equation, font=('Arial', 20), bd=10, insertborderwidth=2, justify='right')
expression_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=20, ipady=20, sticky='nsew')

# Define button colors
button_bg = 'white'
button_fg = 'black'

# Buttons for numbers (0-9)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), (' / ', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), (' * ', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), (' - ', 3, 3),
    ('0', 4, 1), ('.', 4, 0), (' + ', 4, 3)
]

# Create buttons in a loop
for (text, row, column) in buttons:
    btn = Button(gui, text=text, fg=button_fg, bg=button_bg,
                 command=lambda t=text: press(t), height=2, width=8, font=('Arial', 14, 'bold'))
    btn.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

# Clear button
clear_btn = Button(gui, text='Clear', fg='black', bg='orange',
                   command=clear, height=2, width=8, font=('Arial', 14, 'bold'))
clear_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

# Equal button
equal_btn = Button(gui, text='=', fg='black', bg='light green',
                   command=equalpress, height=2, width=8, font=('Arial', 14, 'bold'))
equal_btn.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky='nsew')

# Configure grid rows and columns to expand with window resizing
for i in range(6):
    gui.grid_rowconfigure(i, weight=1)
for i in range(4):
    gui.grid_columnconfigure(i, weight=1)

# Start the GUI
gui.mainloop()

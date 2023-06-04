import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text="Result: " + str(result))
    except:
        output.config(text="Invalid input!")

# Function to insert numbers
def insert_number(number):
    entry.insert(tk.END, number)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget for user input
entry = tk.Entry(window, width=20)
entry.pack()

# Create a button to trigger calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create number buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack()

numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]

for number in numbers:
    button = tk.Button(buttons_frame, text=number, command=lambda num=number: insert_number(num))
    button.pack(side=tk.LEFT)

# Create buttons for additional operations
add_button = tk.Button(buttons_frame, text="+", command=lambda: entry.insert(tk.END, "+"))
add_button.pack(side=tk.LEFT)

subtract_button = tk.Button(buttons_frame, text="-", command=lambda: entry.insert(tk.END, "-"))
subtract_button.pack(side=tk.LEFT)

multiply_button = tk.Button(buttons_frame, text="", command=lambda: entry.insert(tk.END, ""))
multiply_button.pack(side=tk.LEFT)

divide_button = tk.Button(buttons_frame, text="/", command=lambda: entry.insert(tk.END, "/"))
divide_button.pack(side=tk.LEFT)

# Create a label to display the result
output = tk.Label(window, text="Result: ")
output.pack()

# Start the main event loop
window.mainloop()

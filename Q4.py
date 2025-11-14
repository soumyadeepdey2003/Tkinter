from tkinter import *

# Create the main window
root = Tk()
root.title("Background Color Changer")
root.geometry("400x300")

# Variable to store the current color
current_color = StringVar()
current_color.set("white")

# Set initial background color
root.config(bg="white")

# Create a label for instructions
label = Label(root, text="Click Color Buttons to Change Background",
              font=("Arial", 12, "bold"), bg="white")
label.pack(pady=10)

# Create a function to change background color
def change_color(color):
    root.config(bg=color)
    current_color.set(color)
    label.config(bg=color)

# Create buttons for four different colors
button_red = Button(root, text="RED", command=lambda: change_color("red"),
                    font=("Arial", 12, "bold"), bg="red", fg="white",
                    padx=20, pady=10, width=15)
button_red.pack(pady=10)

button_green = Button(root, text="GREEN", command=lambda: change_color("green"),
                      font=("Arial", 12, "bold"), bg="green", fg="white",
                      padx=20, pady=10, width=15)
button_green.pack(pady=10)

button_blue = Button(root, text="BLUE", command=lambda: change_color("blue"),
                     font=("Arial", 12, "bold"), bg="blue", fg="white",
                     padx=20, pady=10, width=15)
button_blue.pack(pady=10)

button_yellow = Button(root, text="YELLOW", command=lambda: change_color("yellow"),
                       font=("Arial", 12, "bold"), bg="yellow", fg="black",
                       padx=20, pady=10, width=15)
button_yellow.pack(pady=10)

# Run the main event loop
root.mainloop()

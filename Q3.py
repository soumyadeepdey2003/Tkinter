from tkinter import *

root = Tk()
root.title("Dropdown Example")

#Create a list of options
options = ["IT", "HR", "Finance", "Sales"]

#Make a variable to track what is selected (type: StringVar)
selected_option = StringVar()
selected_option.set(options[0])
  # default value shown

#Create the dropdown
dropdown = OptionMenu(root, selected_option, *options)
dropdown.pack(pady=10)

#Function to show selection
def show_selection():
    result = selected_option.get()
    label.config(text=f"Selected: {result}")

#Button to trigger display
button = Button(root, text="Show Selected", command=show_selection)
button.pack()

# Label to display the result
label = Label(root, text="Selected: ")
label.pack(pady=10)

root.mainloop()
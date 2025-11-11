from tkinter import *

root = Tk()
root.title("Word Counter")
root.geometry("500x350")

# TITLE
title = Label(root, text="Word Counter", font=("Arial", 16, "bold"))
title.pack()

# INSTRUCTIONS
label1 = Label(root, text="Type text below:")
label1.pack()

# TEXT BOX
text_box = Text(
    root,
    height=10,              
    width=60,                 
)
text_box.pack(padx=10, pady=10)  

# FUNCTION TO COUNT WORDS
# the parameter passed in the function that is event is a special key which denotes whenever any event is going this function will call automatically in this case we bind the function with key press That's why after every key praise the function will call
def count_words(event=None):
    # here inside the gate first 1.0 denotes it start reading from fast line and zeroth character and second parameter that is END-1C denoting that last character will be not taken except all other character will be taken that means we will 
    #skip the last free or new line
    content = text_box.get("1.0", "end-1c")
    words = len(content.split())
    # this line is useful to configure a label named count _label Whenever This name is use for any label the level configure trigger and in this case dynamically fetch the data and write it into text of the label
    count_label.config(text=f"Word Count: {words}")

# BIND TO TEXT BOX
# this will help to bind count words function with text box When hebar key will be press due to this line count words function will be called
text_box.bind("<KeyRelease>", count_words)

# DISPLAY COUNT
count_label = Label(root, text="Word Count: 0", font=("Arial", 12, "bold"), fg="blue")
count_label.pack()

root.mainloop()

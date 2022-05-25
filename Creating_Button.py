from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()

#bg and fg to change color of button and text
myButton = Button(root, text="Click me!", command=myClick, fg="blue", bg="pink")
myButton.pack()

root.mainloop()


from tkinter import *

root = Tk()


#Width to change the width of the entry box
#borderwidth to change to size of the border around the entry box
#fg and bg to change colors

e = Entry(root, width=50, borderwidth=50)
e.pack()
e.insert(0, "Enter your name: ")


def myClick():
    Hello = "Hello " + e.get() + "!"
    myLabel = Label(root, text=Hello)
    myLabel.pack()


myButton = Button(root, text="Enter your name", command=myClick, fg="blue", bg="pink")
myButton.pack()

root.mainloop()
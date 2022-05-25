from tkinter import *

root = Tk()
root.title("Some Fun Radio Buttons")
root.iconbitmap("noun_itsukushima_shrine_2935953_vU0_icon.ico")

#e = IntVar()
#e.set("2")

# Creating a list with different variables
toppings =[
    ("Pepperoni", "Pepperoni"),
    ("Ham", "Ham"),
    ("Cheese", "Cheese"),
    ("Onion", "Onion"),
]
# Sets current topping to pepperoni
pizza = StringVar()
pizza.set("Pepperoni")

# Creating a loop with the list and making radiobuttons
for text, topping in toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)



# A function that checks the value of the radiobutton aka topping
def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

# This is just a simple radiobutton
#Radiobutton(root, text="Option 1", variable=e, value=1, command=lambda: clicked(e.get())).pack()
#Radiobutton(root, text="Option 2", variable=e, value=2, command=lambda: clicked(e.get())).pack()



# Displays current topping choice
Myy_button = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
Myy_button.pack()

mainloop()
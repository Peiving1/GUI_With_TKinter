from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("A fun little frame")
root.iconbitmap("noun_itsukushima_shrine_2935953_vU0_icon.ico")

Gunnis = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
Gunnis.grid(padx=10, pady=10)


# You can use the grid system inside a frame
c = Button(Gunnis, text="Don`t Click Me!")
c.grid(row=0, column=0)
b = Button(Gunnis, text="Do Click Me!")
b.grid(row=1, column=1)





root.mainloop()
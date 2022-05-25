from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap("noun_itsukushima_shrine_2935953_vU0_icon.ico")


# Different kinds of message boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno



def popup():
    response = messagebox.askyesno("This is my Popup!", " Hello World!")


Button(root, text="Popup", command=popup).pack()



mainloop()
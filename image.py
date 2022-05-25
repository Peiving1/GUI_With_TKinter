from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learn To Code at Codemy.com")
root.iconbitmap("D:\PycharmProjects\Tkinter_GUI\\noun_itsukushima_shrine_2935953_vU0_icon.ico")


my_img = ImageTk.PhotoImage(Image.open("Person.jpg"))
my_button = Button(image=my_img)
my_button.grid(row=1,column=0)



button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=0,column=0)






root.mainloop()
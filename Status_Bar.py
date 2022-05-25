from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("D:\PycharmProjects\Tkinter_GUI\\noun_itsukushima_shrine_2935953_vU0_icon.ico")

my_img1 = ImageTk.PhotoImage(Image.open("Images/Art.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/Bridge.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/Fjord.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/Holmen.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/Nipa.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("Images/Plank.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("Images/river.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("Images/snowman.jpg"))

# A list of all the pictures
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8]


my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # Forgets/Deletes what`s on the screen
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 8:
        button_forward = Button(root, text=">>", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    # Update Status Bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)



def back(image_number):
    global my_label
    global button_forward
    global button_back

    # Forgets/Deletes what`s on the screen
    my_label.grid_forget()

    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    # Update Status Bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_back.grid(row=1, column=0)

button_exit = Button(root, text="EXIT", command=root.quit)
button_exit.grid(row=1, column=1)

button_forward = Button(root, text=">>", command=lambda: forward(2))
button_forward.grid(row=1, column=2, pady=10)

# Anchor is to anchor text or image to a place on the grid, N S W E, E=right side
# Relief is a style to the label, SUNKEN, FLAT, RAISED, GROOVE, RIDGE
# len is a function for counting the length of something
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
# Use sticky to stretch over the whole grid, W+E = Left to right
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()

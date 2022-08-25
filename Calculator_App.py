from tkinter import *
import math
from time import sleep

root = Tk()
root.title("A Better Calculator")
root.iconbitmap("D:\PycharmProjects\Tkinter_GUI\\noun_itsukushima_shrine_2935953_vU0_icon.ico")

e = Entry(root, width=30, borderwidth=10)
e.grid(row=0, column=0, columnspan=5)


def button_click(number):
    e.insert(END, number)
    # e.delete(0, END)
    #current = e.get()
    #e.delete(0, END)
    #e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    num1 = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(num1)
    e.delete(0, END)


def button_multiply():
    num1 = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(num1)
    e.delete(0, END)


def button_divide():
    num1 = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(num1)
    e.delete(0, END)


def button_subtract():
    num1 = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = float(num1)
    e.delete(0, END)


def button_equal():
    num2 = e.get()
    e.delete(0, END)
    # e.insert(0, f_num + float(num2))

    if math == "multiply":
        e.insert(0,f_num * float(num2))
    elif math == "addition":
        ans = f_num + float(num2)
        e.insert(0, float(ans))
    elif math == "divide":
        e.insert(0, f_num / float(num2))
    elif math == "subtract":
        e.insert(0, f_num - float(num2))


def button_sqrt():
    num1 = e.get()
    e.delete(0, END)
    num2 = float(num1)
    num2 = num2 ** (1/2)
    e.insert(0, num2)

def button_plus_minus():
    num= float(e.get())
    e.delete(0, END)
    if num >= 0:
        num = str(num)
        e.insert(0, "-"+ num)
    elif num <= 0:
        num = num * -1
        num = str(num)
        e.insert(0, num)

def button_decimal():
    num = e.get()
    e.delete(0, END)
    e.insert(0, num + ".")

def button_mr():
    # Recall the current memory register value
    global memory
    e.delete(0, END)
    e.insert(0, str(memory))


def button_mc():
    # Memory clear, set value to 0
    global memory
    memory = "0"
    display = e.get()
    e.delete(0, END)
    e.insert(0, "Memory Clear")
    #sleep(0.5)
    #e.delete(0, END)
    #e.insert(0, display)
    print(display)


def button_m_add():
    # Add current value to mr
    global memory
    # num1 = e.get()
    memory = float(memory) + float(e.get())


def button_m_sub():
    # Subtract current value from mr
    global memory
    global memory
    memory = float(memory) - float(e.get())

def button_bck():
    num = e.get()
    e.delete(0, END)
    e.insert(0, num[0:-1])


# Define Buttons

button_1 = Button(root, text="1", padx=25, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=25, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=25, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=25, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=25, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=25, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=25, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=25, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=25, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=25, pady=20,
                  command=lambda: button_click(0))
button_add = Button(root, text="+", padx=28, pady=20,
                    command=button_add)
button_clear = Button(root, text="C", padx=41, pady=20,
                      command=button_clear, fg="red")
button_equal = Button(root, text="=", padx=41, pady=20,
                      command=button_equal)
button_subtract = Button(root, text="-", padx=29, pady=20,
                         command=button_subtract)
button_divide = Button(root, text="/", padx=29, pady=20,
                       command=button_divide)
button_multiply = Button(root, text="*", padx=29, pady=20,
                         command=button_multiply)
button_sqrt = Button(root, text="√", padx=24, pady=20,
                     command=button_sqrt)
button_mr = Button(root, text="MR", padx=19, pady=20,
                   command=button_mr)
button_m_add = Button(root, text="M+", padx=20, pady=20,
                      command=button_m_add)
button_mc = Button(root, text="MC", padx=20, pady=20,
                   command=button_mc)
button_m_sub = Button(root, text="M-", padx=20, pady=20,
                      command=button_m_sub)
button_decimal = Button(root, text=".", padx=25, pady=20,
                        command=button_decimal)
button_plus_minus = Button(root, text= "+/-", padx=20, pady=20,
                           command=button_plus_minus)
button_bck = Button(root, text="bck", padx=18, pady=20,
                    command=button_bck)

# Put buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_decimal.grid(row=4,column=2)

button_clear.grid(row=5, column=0, columnspan=2, sticky=W)
button_equal.grid(row=5, column=1, columnspan=2, sticky=E)

button_subtract.grid(row=4, column=3)
button_add.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_plus_minus.grid(row=4, column=0)

button_sqrt.grid(row=5, column=3)

button_mr.grid(row=6, column=0)
button_m_add.grid(row=6, column=1)
button_m_sub.grid(row=6, column=2)
button_mc.grid(row=6, column=3)

button_bck.grid(row=7, column=0)


root.mainloop()
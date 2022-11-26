from tkinter import *
import math
from time import sleep

game = Tk()
game.title("A Better Calculator")
game.iconbitmap("D:\PycharmProjects\Tkinter_GUI\\noun_itsukushima_shrine_2935953_vU0_icon.ico")

# Defines the two different frames, one basic calculator and one to call more advanced functions
calu = LabelFrame(game, text="This a good calculator!", padx=5, pady=5)
calu.grid(row=0, column=0, padx=10, pady=10)

function_btns = LabelFrame(game, text="H", padx=5, pady=5)
function_btns.grid(row=0, column=1,padx=10,pady=10)

e = Entry(calu, width=30, borderwidth=10)
e.grid(row=0, column=0, columnspan=5)


# functions for basic calculator

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


# Define Buttons for basic calculator

button_1 = Button(calu, text="1", padx=25, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(calu, text="2", padx=25, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(calu, text="3", padx=25, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(calu, text="4", padx=25, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(calu, text="5", padx=25, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(calu, text="6", padx=25, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(calu, text="7", padx=25, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(calu, text="8", padx=25, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(calu, text="9", padx=25, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(calu, text="0", padx=25, pady=20,
                  command=lambda: button_click(0))
button_add = Button(calu, text="+", padx=28, pady=20,
                    command=button_add)
button_clear = Button(calu, text="C", padx=41, pady=20,
                      command=button_clear, fg="red")
button_equal = Button(calu, text="=", padx=41, pady=20,
                      command=button_equal)
button_subtract = Button(calu, text="-", padx=29, pady=20,
                         command=button_subtract)
button_divide = Button(calu, text="/", padx=29, pady=20,
                       command=button_divide)
button_multiply = Button(calu, text="*", padx=29, pady=20,
                         command=button_multiply)
button_sqrt = Button(calu, text="√", padx=24, pady=20,
                     command=button_sqrt)
button_mr = Button(calu, text="MR", padx=19, pady=20,
                   command=button_mr)
button_m_add = Button(calu, text="M+", padx=20, pady=20,
                      command=button_m_add)
button_mc = Button(calu, text="MC", padx=20, pady=20,
                   command=button_mc)
button_m_sub = Button(calu, text="M-", padx=20, pady=20,
                      command=button_m_sub)
button_decimal = Button(calu, text=".", padx=25, pady=20,
                        command=button_decimal)
button_plus_minus = Button(calu, text= "+/-", padx=20, pady=20,
                           command=button_plus_minus)
button_bck = Button(calu, text="bck", padx=18, pady=20,
                    command=button_bck)

# Put buttons on the screen for basic calculator

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


# Functions for function_btns label

def pyt():
    pyt_screen = Toplevel()
    pyt_screen.title("Pyt_Calculator")

    pyt = False
    global run

    def button_num(number):
        enter.insert(END, number)

    def button_pyt():
        enter.delete(0,END)
        enter.insert(0, "Enter first num: ")

    def button_ent():
        global pyt
        global num1
        global num2
        mid = enter.get()
        mid = str(mid[6:-6])
        if mid == "first ":
            num1 = enter.get() + " "
            num1 = num1[17:-1]
            enter.delete(0,END)
            enter.insert(0, "Enter second num: ")

        elif mid == "second ":
            num2 = enter.get() + " "
            num2 = num2[18:-1]
            num2 = float(num2)
            num1 = float(num1)
            num3 = num2 ** 2 + num1 ** 2
            num3 = str(num3 ** (1 / 2))
            enter.delete(0, END)
            enter.insert(0, num3)
            print("num1= ", num1, "num2= ", num2)
            print("num3", num3)

        else:
            print(mid)
            print("soy")










    # Define buttons

    enter = Entry(pyt_screen, width=20, borderwidth=10)
    enter.insert(0, "Enter first num: ")

    # numpad
    button_1 = Button(pyt_screen, text="1", padx=20, pady=10,
                      command=lambda: button_num(1))
    button_2 = Button(pyt_screen, text="2", padx=20, pady=10,
                      command=lambda: button_num(2))
    button_3 = Button(pyt_screen, text="3", padx=20, pady=10,
                      command=lambda: button_num(3))
    button_4 = Button(pyt_screen, text="4", padx=20, pady=10,
                      command=lambda: button_num(4))
    button_5 = Button(pyt_screen, text="5", padx=20, pady=10,
                      command=lambda: button_num(5))
    button_6 = Button(pyt_screen, text="6", padx=20, pady=10,
                      command=lambda: button_num(6))
    button_7 = Button(pyt_screen, text="7", padx=20, pady=10,
                      command=lambda: button_num(7))
    button_8 = Button(pyt_screen, text="8", padx=20, pady=10,
                      command=lambda: button_num(8))
    button_9 = Button(pyt_screen, text="9", padx=20, pady=10,
                      command=lambda: button_num(9))
    button_0 = Button(pyt_screen, text="0", padx=20, pady=10,
                      command=lambda: button_num(0))

    button_pyt = Button(pyt_screen, text="reset", padx=4, pady=10,
                        command=button_pyt)
    button_ent = Button(pyt_screen, text="ent", padx=10, pady=10,
                        command=button_ent)

    # Put buttons on screen

    button_1.grid(row=3, column=2)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=0)
    button_4.grid(row=2, column=2)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=0)
    button_7.grid(row=1, column=2)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=0)
    button_0.grid(row=4, column=1)

    button_pyt.grid(row=1, column=3)
    button_ent.grid(row=2, column=3)
    enter.grid(row=0, column=0, columnspan=3)

    pyt_screen.mainloop()



# define buttons function_btns label

button_pyt = Button(function_btns, text="pyt", padx=10, pady=10, command=pyt)
button_log = Button(function_btns, text="log", padx=10, pady=10)

# Put buttons on function_btns label

button_pyt.grid(row=0,column=0)
button_log.grid(row=1, column=0)

game.mainloop()
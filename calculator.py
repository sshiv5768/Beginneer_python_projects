import tkinter as tk
from tkinter import *


def btn_clicked(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)


def btn_clear():
    global operator
    operator = ""
    text_Input.set("")


def btn_equal():
    global operator
    summation = str(eval(operator))
    text_Input.set(summation)
    operator = ''


top = Tk()
top.title("Calculator")
operator = ""
text_Input = StringVar()
textDisplay = Entry(top, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="#ffb233", justify='right').grid(columnspan=4)

btn1 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked(1), text="1").grid(row=1, column=0)
btn2 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked(2), text="2").grid(row=1, column=1)
btn3 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked(3), text="3").grid(row=1, column=2)
btn_plus = Button(top, padx=16, bd=8, fg="black", bg="#ffb233", font=('arial', 20, 'bold'), command=lambda: btn_clicked('+'),  text="+").grid(row=1, column=3)
# =========================== || ==============================

btn4 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked(4), text="4").grid(row=2, column=0)
btn5 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked(5), text="5").grid(row=2, column=1)
btn6 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked(6), text="6").grid(row=2, column=2)
btn_minus = Button(top, padx=16, bd=8, fg="black", bg="#ffb233", font=('arial', 20, 'bold'), command=lambda: btn_clicked('-'), text="-").grid(row=2, column=3)

# ============================= || ============================

btn7 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked(7), text="7").grid(row=3, column=0)
btn8 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked(8), text="8").grid(row=3, column=1)
btn9 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked(9), text="9").grid(row=3, column=2)
btn_divide = Button(top, padx=16, bd=8, fg="black", bg="#ffb233", font=('arial', 20, 'bold'), command=lambda: btn_clicked('/'), text="/").grid(row=3, column=3)

# ==================================== || ======================

btn0 = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'),  command=lambda: btn_clicked(0), text="0").grid(row=4, column=0)
btn_pers = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=lambda: btn_clicked('%'), text="%").grid(row=4, column=1)
btn_equal = Button(top, padx=16, bd=8, fg="black", bg="#33ff83", font=('arial', 20, 'bold'), command=btn_equal, text="=").grid(row=4, column=2)
btn_multiplication = Button(top, padx=16, bd=8, fg="black", bg="#ffb233", font=('arial', 20, 'bold'), command=lambda: btn_clicked('*'), text="*").grid(row=4, column=3)

# =================================== || =======================

btn_clear = Button(top, padx=16, pady=16, bd=8, fg="black", bg="#ffb233", font=('arial', 20, 'bold'), command=btn_clear, text="C").grid(row=5, column=0)


top.mainloop()
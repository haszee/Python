import tkinter as tk

expression = ""

def clear():
	global expression
	expression = ""
	text_box.delete(1.0,"end")

def delete():
	global expression
	expression = expression[:-1]
	text_box.delete(1.0,"end")
	text_box.insert(1.0,expression)

def calc_expression(symbol):
	global expression
	expression += str(symbol)
	text_box.delete(1.0,"end")
	text_box.insert(1.0,expression)


def evaluate_calc():
	global expression
	try:
		expression = str(eval(expression))
		text_box.delete(1.0,"end")
		text_box.insert(1.0,expression)

	except:
		clear()
		text_box.insert(1.0,"ERROR")

root = tk.Tk()
root.geometry("500x375")


text_box = tk.Text(root, height=2, width = 27, font=("Arial",24))
text_box.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: calc_expression(1), width=5, font=("Arial",14))
btn_1.grid(row=2, column=0)

btn_2 = tk.Button(root, text="2", command=lambda: calc_expression(2), width=5, font=("Arial",14))
btn_2.grid(row=2, column=1)

btn_3 = tk.Button(root, text="3", command=lambda: calc_expression(3), width=5, font=("Arial",14))
btn_3.grid(row=2, column=2)

btn_4 = tk.Button(root, text="4", command=lambda: calc_expression(4), width=5, font=("Arial",14))
btn_4.grid(row=3, column=0)

btn_5 = tk.Button(root, text="5", command=lambda: calc_expression(5), width=5, font=("Arial",14))
btn_5.grid(row=3, column=1)

btn_6 = tk.Button(root, text="6", command=lambda: calc_expression(6), width=5, font=("Arial",14))
btn_6.grid(row=3, column=2)

btn_7 = tk.Button(root, text="7", command=lambda: calc_expression(7), width=5, font=("Arial",14))
btn_7.grid(row=4, column=0)

btn_8 = tk.Button(root, text="8", command=lambda: calc_expression(8), width=5, font=("Arial",14))
btn_8.grid(row=4, column=1)

btn_9 = tk.Button(root, text="9", command=lambda: calc_expression(9), width=5, font=("Arial",14))
btn_9.grid(row=4, column=2)

btn_0 = tk.Button(root, text="0", command=lambda: calc_expression(0), width=5, font=("Arial",14))
btn_0.grid(row=5, column=1)

btn_plus = tk.Button(root, text="+", command=lambda: calc_expression("+"), width=5, font=("Arial",14))
btn_plus.grid(row=2, column=3)

btn_minus = tk.Button(root, text="-", command=lambda: calc_expression("-"), width=5, font=("Arial",14))
btn_minus.grid(row=3, column=3)

btn_multiply = tk.Button(root, text="*", command=lambda: calc_expression("*"), width=5, font=("Arial",14))
btn_multiply.grid(row=4, column=3)

btn_divide = tk.Button(root, text="/", command=lambda: calc_expression("/"), width=5, font=("Arial",14))
btn_divide.grid(row=5, column=3)

btn_exp = tk.Button(root, text="^", command=lambda: calc_expression("^"), width=5, font=("Arial",14))
btn_exp.grid(row=6, column=1)

btn_factorial = tk.Button(root, text="!", command=lambda: calc_expression("!"), width=5, font=("Arial",14))
btn_factorial.grid(row=6, column=2)

btn_bracket_left = tk.Button(root, text="(", command=lambda: calc_expression("("), width=5, font=("Arial",14))
btn_bracket_left.grid(row=5, column=0)

btn_bracket_right = tk.Button(root, text=")", command=lambda: calc_expression(")"), width=5, font=("Arial",14))
btn_bracket_right.grid(row=5, column=2)

btn_decimal = tk.Button(root, text=".", command=lambda: calc_expression("."), width=5, font=("Arial",14))
btn_decimal.grid(row=6, column=0)

btn_equal = tk.Button(root, text="=", command=evaluate_calc, width=5, font=("Arial",14))
btn_equal.grid(row=6, column=3)

btn_delete = tk.Button(root, text="DEL", command=delete, width=5, font=("Arial",14))
btn_delete.grid(row=7, column=3)

btn_clear = tk.Button(root, text="C", command=clear, width=5, font=("Arial",14))
btn_clear.grid(row=7, column=0)


root.mainloop()
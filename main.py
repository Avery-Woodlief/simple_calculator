import json
import math

with open("colors.json", "r") as f:
    COLORS = json.load(f)
BUTTON_SIZE_NORMAL = (44, 69) # height, width


class Button:
    def __init__(self, **kwargs):
        # name, size, row, col, rowspan, colspan, color
        
        if kwargs.get("color", None) == None:
            raise ValueError("color not specified")


        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.color_active = COLORS[self.color]["window_unfocus"]

    

    def __str__(self):
        string = ""
        for var in self.__dict__:
            string += f"{var}={getattr(self, var)}\n"
        return string
integer_buttons = {}
integer_buttons["zero"] = Button(name="0", size=BUTTON_SIZE_NORMAL, row=4, col=0, color="white")
integer_buttons["one"] = Button(name="1", size=BUTTON_SIZE_NORMAL, row=3, col=0, color="white")
integer_buttons["two"] = Button(name="2", size=BUTTON_SIZE_NORMAL, row=3, col=1, color="white")
integer_buttons["three"] = Button(name="3", size=BUTTON_SIZE_NORMAL, row=3, col=2, color="white")
integer_buttons["four"] = Button(name="4", size=BUTTON_SIZE_NORMAL, row=2, col=0, color="white")
integer_buttons["five"] = Button(name="5", size=BUTTON_SIZE_NORMAL, row=2, col=1, color="white")
integer_buttons["six"] = Button(name="6", size=BUTTON_SIZE_NORMAL, row=2, col=2, color="white")
integer_buttons["seven"] = Button(name="7", size=BUTTON_SIZE_NORMAL, row=1, col=0, color="white")
integer_buttons["eight"] = Button(name="8", size=BUTTON_SIZE_NORMAL, row=1, col=1, color="white")
integer_buttons["nine"] = Button(name="9", size=BUTTON_SIZE_NORMAL, row=1, col=2, color="white")

binary_operation_buttons = {}
binary_operation_buttons["mod"] = Button(name="mod", size=BUTTON_SIZE_NORMAL, row=0, col=3, color="white")
binary_operation_buttons["division"] = Button(name="÷", size=BUTTON_SIZE_NORMAL, row=1, col=3, color="white")
binary_operation_buttons["multiplication"] = Button(name="×", size=BUTTON_SIZE_NORMAL, row=2, col=3, color="white")
binary_operation_buttons["subtraction"] = Button(name="-", size=BUTTON_SIZE_NORMAL, row=3, col=3, color="white")
binary_operation_buttons["addition"] = Button(name="+", size=BUTTON_SIZE_NORMAL, row=4, col=3, color="white")

unary_operation_buttons = {}
unary_operation_buttons["square root"] = Button(name="√", size=BUTTON_SIZE_NORMAL, row=1, col=4, color="white")
unary_operation_buttons["square"] = Button(name="x²", size=BUTTON_SIZE_NORMAL, row=2, col=4, color="white")
unary_operation_buttons["percent"] = Button(name="%", size=BUTTON_SIZE_NORMAL, row=4, col=2, color="white")

special_buttons = {}
special_buttons["pi"] = Button(name="π", size=BUTTON_SIZE_NORMAL, row=0, col=4, color="white")
special_buttons["open_parenthesis"] = Button(name="(", size=BUTTON_SIZE_NORMAL, row=0, col=1, color="white")
special_buttons["close_parenthesis"] = Button(name=")", size=BUTTON_SIZE_NORMAL, row=0, col=2, color="white")
special_buttons["CLEAR"] = Button(name="⌫", size=BUTTON_SIZE_NORMAL, row=0, col=0, color="red")
special_buttons["EQUALS"] = Button(name="=", size=BUTTON_SIZE_NORMAL, row=3, col=4, rowspan=2, color="green")
special_buttons["decimal"] = Button(name=".", size=BUTTON_SIZE_NORMAL, row=4, col=1, color="white")

simple_calculator_buttons = integer_buttons | binary_operation_buttons | unary_operation_buttons | special_buttons
button_names = list(simple_calculator_buttons.keys())

import tkinter as tk
from tkinter import ttk
import re

number_mapping = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9", "pi":"π"}

binary_operation_mapping = {"multiplication":"*", "division":"/", "addition":"+", "subtraction":"-", "mod":"%"}

unary_operation_mapping = {"square root":"math.sqrt(", "square":"**2", "percent":"/100"}

special_chars_mapping = {"decimal":".", "close_parenthesis":")", "open_parenthesis":"("}


class Calculator(tk.Tk):
    def __init__(self,title="title", **kw):
        super().__init__(**kw)
        self.title(title)
        self.geometry("364x461")
        self.expression = tk.StringVar(value="")
        self.logs = []
        self.tree_logs = None
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#fafafa",
            fieldbackground="#fafafa",
            foreground="black"
        )
        self.init_display()
        self.init_buttons()
        

    def feed_clicked_button_name(self, button_name):
        print(self.logs)
        if number_mapping.get(button_name, None) is not None:       
            self.expression.set(self.expression.get() + number_mapping[button_name])
        elif binary_operation_mapping.get(button_name, None) is not None:
            self.expression.set(self.expression.get() + binary_operation_mapping[button_name])
        elif unary_operation_mapping.get(button_name, None) is not None:
            if button_name == "square root":
                self.expression.set(unary_operation_mapping[button_name] + self.expression.get() + ")")
            elif button_name == "square":
                self.expression.set("(" + self.expression.get() + ")" + unary_operation_mapping[button_name])
            elif button_name == "percent":
                self.expression.set("(" + self.expression.get() + ")" + unary_operation_mapping[button_name])
        elif special_chars_mapping.get(button_name, None) is not None:
            self.expression.set(self.expression.get() + special_chars_mapping[button_name])

        if button_name == "EQUALS":
            try:
                result = eval(str(re.sub(re.escape("π"), str(math.pi), self.expression.get())))
                print(f"result = {result}")
                self.logs.append(self.expression.get()+ " = " +str(result))
                self.tree_logs.insert('', 'end', text=self.logs[-1])
                self.expression.set(str(result))
            except (SyntaxError, TypeError):
                if self.expression == "":
                    return
                self.expression.set("malformed expression")
        elif button_name == "CLEAR":
            self.expression.set("")


    def init_buttons(self):
        buttons_frame = tk.Frame(self)
        for i in range(5):
            buttons_frame.columnconfigure(i, weight=1)
            buttons_frame.rowconfigure(i, weight=1)

        for button_name in button_names:
            info = simple_calculator_buttons[button_name]

            button = tk.Button(
                buttons_frame,
                text=info.name,
                font=("Arial", 14),

                # Normal background
                bg=COLORS[info.color]["window_focus"],

                # Mouse-down/active background
                activebackground=COLORS[info.color]["click"],

                fg="white" if button_name=="CLEAR" or button_name=="EQUALS" else "black",
                activeforeground="black",

                command=lambda name=button_name:self.feed_clicked_button_name(name),
                width=simple_calculator_buttons[button_name].size[0],
                height=simple_calculator_buttons[button_name].size[1]
            )
            button.grid(row=simple_calculator_buttons[button_name].row, column=simple_calculator_buttons[button_name].col, rowspan=1 if button_name != "EQUALS" else 2)
            buttons_frame.pack()
            self.update()


    def init_display(self):
        display_frame = tk.Frame(self)
        self.tree_logs = ttk.Treeview(display_frame, height=6, show="tree")

        self.tree_logs.pack(fill="x", anchor="n")
        label = tk.Label(
            display_frame,
            textvariable=self.expression,
            font=("Arial", 14),
            background="white",
            anchor="w",
            padx=15,
            pady=24
        )
        label.pack(fill="both")
        display_frame.pack(fill="both")
        self.update()

if __name__ == "__main__":
    calc = Calculator(title="Calculator")
    calc.mainloop()

"""GUI practise. Craeting a miles to KM converter."""
from tkinter import *


def convert_to_km():
    miles = float(user_input.get())
    km = miles * 1.609
    lbl_output.config(text=str(km))


# window
window = Tk()
window.title("Lily Converter")
window.config(padx=20, pady=20)

# Entry/Input
user_input = Entry(width=5)
user_input.grid(column=1, row=0)

# labels
lbl_miles = Label(text="Miles")
lbl_miles.grid(column=2, row=0)

lbl_km = Label(text="KM")
lbl_km.grid(column=2, row=1)

lbl_is_equal = Label(text="is equal to")
lbl_is_equal.grid(column=0, row=1)

lbl_output = Label(text='0')
lbl_output.grid(column=1, row=1)

# button
btn_calculate = Button(text="Calculate", command=convert_to_km)
btn_calculate.grid(column=1, row=2)

window.mainloop()

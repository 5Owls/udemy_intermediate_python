from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 8
list_reps = []
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(count_text, text="00:00")
    lbl_timer.config(text="Timer")
    lbl_tick.config(text="")
    global reps
    global list_reps
    reps = 8
    list_reps = []


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global list_reps
    if reps == 8 or reps == 6 or reps == 4 or reps == 2:
        count_down(WORK_MIN * 60)
        lbl_timer.config(text="WORK", font=(FONT_NAME, 50, "bold"), fg=PINK)
    elif reps == 7 or reps == 5 or reps == 3:
        count_down(SHORT_BREAK_MIN * 60)
        list_reps.append("✔️")
        lbl_tick.config(text=list_reps)
        lbl_timer.config(text="5Break", font=(FONT_NAME, 50, "bold"), fg=RED)
    elif reps == 1:
        count_down(LONG_BREAK_MIN * 60)
        lbl_timer.config(text="20Break", font=(FONT_NAME, 50, "bold"), fg=GREEN)
    reps = reps - 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(count_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:  # after the first run down
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Udemy Pomodorro")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img_tomato)
count_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

lbl_timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"))
lbl_timer.grid(column=1, row=0)
lbl_timer.config(fg=GREEN, bg=YELLOW)

lbl_tick = Label(fg=RED, bg=YELLOW)
lbl_tick.grid(column=1, row=4)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)
btn_start.config(font=(FONT_NAME, 15, "bold"))

btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(column=2, row=2)
btn_reset.config(font=(FONT_NAME, 15, "bold"))

window.mainloop()

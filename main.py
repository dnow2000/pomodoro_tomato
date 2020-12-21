from tkinter import *
import math

YELLOW = "#ffd803"
ORANGE = "#ff8906"
GREEN = "#2cb67d"
DARK_GREEN = "#00473e"
FONT = "Courier"

WORK_MIN = 25
BREAK_MIN = 5
LONG_BREAK = 20
reps = 0
timer = None


# -------------------------- Timer Mechanism ---------------------------------------------
def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0:
        title_label.config(text="LONG BREAK")
        count_down(LONG_BREAK * 60)
    elif reps % 2 == 0:
        title_label.config(text="BREAK")
        count_down(BREAK_MIN * 60)
    else:
        title_label.config(text="WORK")
        count_down(WORK_MIN * 60)


# -------------------------- Countdown Mechanism -----------------------------------------
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)

        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# -------------------------- Timer Reset -------------------------------------------------
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")
    check_marks.config(text="")
    global reps
    reps = 0

# -------------------------- UI -------------------------------------------------
window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=20, pady=10)

canvas = Canvas(width=332, height=340, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato_img.png")
canvas.create_image(170, 170, image=tomato_img)
timer_text = canvas.create_text(175, 190, text="00:00", fill="white", font=(FONT, 35, "bold"))
canvas.grid(column=2, row=1)

title_label = Label(text="Timer", bg=YELLOW, fg=ORANGE, font=(FONT, 45, "bold"))
title_label.grid(column=2, row=0)

start_button = Button(text="Start", bg=GREEN, fg="white", font=(FONT, 15, "bold"), command=start_timer)
start_button.grid(column=1, row=2)

reset_button = Button(text="Reset", bg=GREEN, fg="white", font=(FONT, 15, "bold"), command=reset_timer)
reset_button.grid(column=3, row=2)

check_marks = Label(fg=DARK_GREEN, bg=YELLOW, font=(FONT, 25, "bold"))
check_marks.grid(column=2, row=2, pady=(16, 0))

canvas.grid()

window.mainloop()

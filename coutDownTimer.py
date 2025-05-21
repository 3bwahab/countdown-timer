import tkinter as tk
from tkinter import messagebox
import time
import threading

def start_timer():
    try:
        t = int(entry.get())
        if t <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer.")
        return

    
    start_btn.config(state="disabled")
    entry.config(state="disabled")

    def countdown():
        while t_container[0] > 0:
            mins, secs = divmod(t_container[0], 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            time_label.config(text=timer_display)
            time.sleep(1)
            t_container[0] -= 1

        time_label.config(text="00:00")
        messagebox.showinfo("Time's up!", "time limit out")
        start_btn.config(state="normal")
        entry.config(state="normal")

    
    t_container[0] = t
    threading.Thread(target=countdown, daemon=True).start()


root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="#2c3e50")


FONT_LARGE = ("Helvetica", 36, "bold")
FONT_MEDIUM = ("Helvetica", 14)


title_label = tk.Label(root, text="Enter time in seconds:", font=FONT_MEDIUM, fg="white", bg="#2c3e50")
title_label.pack(pady=(20, 5))


entry = tk.Entry(root, font=("Helvetica", 18), justify="center")
entry.pack()


start_btn = tk.Button(root, text="Start Countdown", font=FONT_MEDIUM, bg="#1abc9c", fg="white", command=start_timer)
start_btn.pack(pady=10)


time_label = tk.Label(root, text="00:00", font=FONT_LARGE, fg="#e74c3c", bg="#2c3e50")
time_label.pack(pady=10)


t_container = [0]


root.mainloop()

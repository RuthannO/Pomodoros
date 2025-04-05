import tkinter as tk
from tkinter import ttk
import time
from threading import Thread
from ttkthemes import ThemedTk
import sys
import os

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller extracts here
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class PomodoroTimer:
    
    def __init__(self, root):
        # Initialize main window
        self.root = root
        icon_path = resource_path('images/icon.png')
        icon_image = tk.PhotoImage(file=icon_path)
        self.root.iconphoto(False, icon_image)
        self.root.title(" Pomodoro Timer")
        self.root.geometry("500x300")
        self.root.configure(bg='#F0F8FF')
        self.root.resizable(False, False)
    

        # Timer control variables
        self.running = False
        self.work_duration = 25 * 60
        self.break_duration = 5 * 60
        self.time_left = self.work_duration

        # Timer display label
        self.timer_label = tk.Label(
            root, text=self.format_time(self.time_left),
            font=("Segoe UI", 52, "bold"), bg='#F0F8FF', fg='#333')
        self.timer_label.pack(pady=20)

        # Button style
        style = ttk.Style()
        style.configure('TButton', font=('Segoe UI', 14), padding=5)

        # Container for buttons
        buttons_frame = tk.Frame(root, bg='#F0F8FF')
        buttons_frame.pack(pady=10)

        # Control buttons
        self.start_button = ttk.Button(buttons_frame, text="▶️ Start", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = ttk.Button(buttons_frame, text="⏸ Pause", command=self.pause_timer)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.reset_button = ttk.Button(buttons_frame, text="🔄 Reset", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=5)

    def format_time(self, seconds):
        # Format seconds to MM:SS
        return time.strftime('%M:%S', time.gmtime(seconds))

    def update_timer(self):
        # Update timer every second
        while self.running and self.time_left:
            time.sleep(1)
            self.time_left -= 1
            self.timer_label.config(text=self.format_time(self.time_left))

        # Switch modes when timer ends
        if self.time_left == 0:
            self.running = False
            self.switch_mode()

    def switch_mode(self):
        # Switch between work and break durations
        if self.time_left == 0:
            if self.time_left == self.work_duration:
                self.time_left = self.break_duration
            else:
                self.time_left = self.work_duration

            self.timer_label.config(text=self.format_time(self.time_left))

    def start_timer(self):
        # Start timer thread
        if not self.running:
            self.running = True
            Thread(target=self.update_timer).start()

    def pause_timer(self):
        # Pause timer
        self.running = False

    def reset_timer(self):
        # Reset timer to initial work duration
        self.running = False
        self.time_left = self.work_duration
        self.timer_label.config(text=self.format_time(self.time_left))

if __name__ == '__main__':
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()

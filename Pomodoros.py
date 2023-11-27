import tkinter as tk
import time
from threading import Thread


class PomodoroTimer:
#__init__ pretty much stands for initializing, it initializes the class, sets up the initial state of the pomodoro timer.

    def __init__(self, tkwindow):


# "self" is refering to this class, "PomodoroTimer", self.tkwindow is an instance attribute for PomodoroTimer. it
# becomes an attribute of the class instance. This means any method within the PomodoroTimer class can access
# self.tkwindow and, therefore, interact with the tkinter window. It is unique to each instance and can be used in
# any method of the class to access or modify the tkinter window. tkwindow without 'self' is a local variable to
# __init__ and is limited to this method's scope. self.tkwindow allows the PomodoroTimer object to remember and
# utilize the tkinter window for its operations like displaying timers and buttons.

        self.tkwindow = tkwindow
        self.tkwindow.title("Pomodoro Timer")


#self.state = False is setting the initial state of the timer to "not running" when an instance of the class is created.

        self.state = False
# Since there are 60 seconds in a minute, to convert 25 minutes into seconds, you multiply 25 by 60. This gives you
# the total number of seconds in 25 minutes.

        self.work_time = 30 * 60
        self.break_time = 10 * 60

# this is setting the current time as 30 minutes, when the timer starts to count down it will actively show it,
# in other words this is necessary to keep track of the time

        self.current_time = self.work_time
        self.display_time = self.current_time

#this section is responsible for creating and displaying the labels and buttons in the GUI

        self.timer_label = tk.Label(self.tkwindow, text=self.format_time(self.display_time), font=("Helvetica",48))
        self.timer_label.pack()

        self.start_button = tk.Button(self.tkwindow, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.pause_button = tk.Button(self.tkwindow, text="Pause", command=self.pause_time)
        self.pause_button.pack()

        self.reset_button = tk.Button(self.tkwindow, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

#text formatting in tkwindow
    def format_time(self,seconds):
    #"Return" in programming isn't quite like a "continue" button.
    #It's actually more like an "exit" button that also has the ability to hand you something on the way out.
        return time.strftime('%M:%S',time.gmtime(seconds))
    def update_timer(self):
        while self.state:
            self.display_time -= 1
            time.sleep(1)
            self.timer_label.config(text=self.format_time(self.display_time))
            self.tkwindow.update()
            if self.display_time == 0:
                self.state=False
#
                self.current_time = self.break_time if self.current_time == self.work_time else self.work_time
                self.display_time = self.current_time



    def start_timer(self):

        if not self.state:
            self.state= True
            self.thread = Thread(target=self.update_timer)
            self.thread.start()

    def reset_timer(self):
        self.state=False
        self.display_time = self.work_time
        self.timer_label.config(text=self.format_time(self.display_time))

    def pause_time(self):
        self.state = False

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()

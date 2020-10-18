from tkinter import *
import datetime
import time
import pygame


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            pygame.mixer.init()
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play()
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title("Alarm Clock")
clock.geometry("350x250")
time_format = Label(clock, text="Enter time in 24 hour format!",
                    fg="red", bg="blue", font="Arial").place(x=50, y=140)
addTime = Label(clock, text="Hour  Min   Sec", font=60).place(x=150, y=20)
setYourAlarm = Label(clock, text="When to wake you up", fg="blue",
                     relief="solid", font=("Arial", 8, "bold")).place(x=10, y=50)


# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

# Time required to set the alarm clock:
hourTime = Entry(clock, textvariable=hour, bg="pink",
                 width=5).place(x=150, y=50)
minTime = Entry(clock, textvariable=min, bg="pink",
                width=5).place(x=190, y=50)
secTime = Entry(clock, textvariable=sec, bg="pink",
                width=5).place(x=230, y=50)

# To take the time input by user:
submit = Button(clock, text="Set Alarm", fg="red", width=10,
                command=actual_time).place(x=110, y=90)


# Execution of the window.
clock.mainloop()

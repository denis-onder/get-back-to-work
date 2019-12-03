import psutil
import os
from threading import Timer
import random

delay = 300.0


def check_if_working():
    # Check if Visual Studio Code is running
    if "code" in (p.name() for p in psutil.process_iter()):
        print("The user is working. Leave it be.")
    else:
        os.system('code && notify-send "GET BACK TO WORK"')


def set_interval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, set_interval, [timer, task]).start()


if __name__ == "__main__":
    set_interval(delay, check_if_working)

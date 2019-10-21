import psutil
import os
from threading import Timer
import random

delay = 300.0


def check_if_working():
    if "code" in (p.name() for p in psutil.process_iter()):
        print("The poor human being is working. Leave him be.")
    else:
        os.system('code && notify-send "GET BACK TO WORK"')


def set_interval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, set_interval, [timer, task]).start()


if __name__ == "__main__":
    set_interval(delay, check_if_working)

import subprocess
import time
from Util.adb import ADB


class TouchPoint:

    def __init__(self, x, y, sleep=1):
        self.x = x
        self.y = y
        self.sleep = sleep

    def offset(self, point):
        return TouchPoint(self.x + point.x, self.y + point.y)

    def touch(self):
        print("tap: {} {}".format(self.x, self.y))
        ADB.Input.tap(self.x, self.y)
        time.sleep(self.sleep)

import subprocess
import time


class TouchPoint:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def offset(self, point):
        return TouchPoint(self.x + point.x, self.y + point.y)

    def touch(self):
        cmd = "adb shell input tap {} {}".format(self.x, self.y)
        print("Executing: " + cmd)
        subprocess.check_output(cmd)
        time.sleep(1)

from Util.adb import ADB
import numbers
import time


class Routine(object):
    """docstring for Routine"""

    def __init__(self):
        return

    def tap(self, steps):
        for step in steps:
            if isinstance(step, list):
                if len(step) is 2:
                    ADB.Input.tap(step[0], step[1])

            elif isinstance(step, numbers.Number):
                time.sleep(step)

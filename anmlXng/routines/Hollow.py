from Util.adb import ADB_Input
from Models.Routine import Routine


class HollowRoutine(Routine):

    def __init__(self, anmlXng):
        super().__init__()
        self.anmlXng = anmlXng

    def collect(self, fruit):
        method = getattr(self, collect + fruit.title())
        if callable(method):
            method()

    def

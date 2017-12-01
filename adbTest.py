from Util.adb import ADB
import sys
import time

#adb = ADB()
#fs = ADB_File()
args = sys.argv
del(args[0])
l = len(args)
if l > 0:
    cmd = args[0].lower()
    del(args[0])
    l = len(args)
    if cmd == "tap" and l is 2:
        ADB.Input.tap(*args)
    elif cmd == "shot" and l is 1:
        t0 = time.time()
        ADB.Screen.shot2file(args[0], True, True)
        t1 = time.time()
        print("Elapsed: %f" % (t1 - t0))


# print(adb.devices())

# print(fs.ls(""))

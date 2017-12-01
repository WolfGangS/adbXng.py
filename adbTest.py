from Util.adb import ADB, ADB_File, ADB_Screen, ADB_Input
import sys
import time

#adb = ADB()
#fs = ADB_File()
args = sys.argv
del(args[0])
l = len(args)
if l > 0 :
	cmd = args[0].lower()
	del(args[0])
	l = len(args)
	if cmd == "tap" and l is 2:
		ADB_Input.tap(*args)

time.sleep(5)

ADB_Screen.shot2file("__shot.png",True)

#print(adb.devices())

#print(fs.ls(""))


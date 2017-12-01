import subprocess
import os
import time

class ADB(object):
	"""docstring for ADB"""
	def call(cmd):
		cmd = "adb " + cmd
		print(cmd)
		return subprocess.check_output(cmd.split())

	def shell(cmd):
		return ADB.call("shell " + cmd)

	def devices():
		raw = ADB.call("devices").decode("utf-8").strip().split("\n");
		devices = {}
		for i in range(1,len(raw)):
			line = raw[i].split("\t")
			if len(line) is 2:
				devices[line[0]] = line[1]

		return devices



class ADB_Input(object):
	"""docstring for ADB_Input"""
	def input(cmd):
		return ADB.shell("input " + cmd)

	def tap(x,y):
		ADB_Input.input("tap {} {}".format(x,y))

	def swipe(sx,sy,ex,ey,d):
		ADB_Input.input("swipe {} {} {} {} {}".format(sx,sy,ex,ey,d))

	def longpress(x,y,d):
		ADB_Input.swipe(x,y,x,y,d)

	def text(txt):
		ADB_Input.input('text "' + txt.replace('"','\\"') + '"')

	def keyevent(key_code):
		ADB_Input.input("keyevent " + key_code)



class ADB_File(object):
	"""docstring for ADB_File"""
	def push(frm,to):
		return ADB.call("push {} {}".format(frm,to))

	def pull(frm,to):
		return ADB.call("pull {} {}".format(frm,to))

	def ls(path = ""):
		return ADB.shell("ls /sdcard/" + path.lstrip("/")).decode("utf-8").strip().split(os.linesep)

	def rm(path):
		return ADB.shell("rm " + path)


class ADB_Screen(object):
	def shot(path="-p"):
		return ADB.shell("screencap " + path)

	def shot2file(file,local = False, via_pull = False):
		if local and not via_pull:
			img = ADB_Screen.shot()
			if os.linesep is "\r\n":
				img = img.replace(b'\r\n',b'\n')
			img_file = open(file,"wb")
			img_file.write(img)
			img_file.close()
		elif local:
			fn = "/sdcard/adbshot_{}.png".format(int(time.time()))
			ADB_Screen.shot(fn)
			ADB_File.pull(fn,file)
			ADB_File.rm(fn)
		else :
			return ADB_Screen.shot(file)

	def record(file,length = 5):
		return ADB.shell("screenrecord --time-limit {} {}".format(length,file))




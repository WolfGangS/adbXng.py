import subprocess
import os
import time

class ADB(object):
	"""docstring for ADB"""
	def call(self,cmd):
		cmd = "adb " + cmd
		return subprocess.check_output(cmd.split())

	def shell(self,cmd):
		return self.call("shell " + cmd)

	def devices(self):
		raw = self.call("devices").decode("utf-8").strip().split("\n");
		devices = {}
		for i in range(1,len(raw)):
			line = raw[i].split("\t")
			if len(line) is 2:
				devices[line[0]] = line[1]

		return devices



class ADB_Input(ADB):
	"""docstring for ADB_Input"""
	def input(self,cmd):
		return self.shell("input " + cmd)

	def tap(self,x,y):
		self.input("tap {} {}".format(x,y))

	def swipe(self,sx,sy,ex,ey,d):
		self.input("swipe {} {} {} {} {}".format(sx,sy,ex,ey,d))

	def longpress(self,x,y,d):
		self.swipe(x,y,x,y,d)

	def text(self,txt):
		self.input('text "' + txt.replace('"','\\"') + '"')

	def keyevent(self, key_code):
		self.input("keyevent " + key_code)



class ADB_File(ADB):
	"""docstring for ADB_File"""
	def push(self,frm,to):
		return self.call("push {} {}".format(frm,to))

	def pull(self,frm,to):
		return self.call("pull {} {}".format(frm,to))

	def ls(self,path = ""):
		return self.shell("ls /sdcard/" + path.lstrip("/")).decode("utf-8").strip().split(os.linesep)

	def rm(self,path):
		return self.shell("rm " + path)


class ADB_Screen(ADB):
	def shot(self,path="-p"):
		return self.shell("screencap " + path)

	def shot2file(self,file,local = False, via_pull = False):
		if local and not via_pull:
			img = self.shot().replace(b'\r\n',b'\n');
			img_file = open(file,"wb")
			img_file.write(img)
			img_file.close()
		elif local:
			fn = "/sdcard/adbshot_{}.png".format(int(time.time()))
			self.shot(fn)
			f = ADB_File()
			f.pull(fn,file)
			f.rm(fn)
		else :
			return self.shot(file)

	def record(self,file,length = 5):
		return self.shell("screenrecord --time-limit {} {}".format(length,file))




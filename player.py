import url_shortener
import config
from speech import speak
import sound_lib
from sound_lib import output
from sound_lib import stream
class status(object):
	def __init__(self):
		self.loaded=False
		self.streaming=False
		self.orig_stream=0
		self.stream=0
		self.url=""

filename=""
p=status()
o=output.Output()

def open_stream(filen=""):
	url = url_shortener.unshorten(filen)
	p.stream =stream.URLStream(url=filen)
	p.streaming=True
	p.url=filen
	config.appconfig['general']['last']=p.url
	p.loaded=True
	p.stream.volume=config.appconfig['general']['volume']
	play()

def play():
	if not p.stream==0:
		p.stream.play()

def stop():
	if not p.stream==0:
		p.stream.stop()
		p.stream.set_position(0)
		p.streaming=false

def devices():
	return o.get_device_names()

def get_device(device=-1):
	if device==-1:
		device=config.appconfig['general']['device']
	devs=devices()
	for i in range(len(devs)):
		if device==devs[i]:
			return i+1
	return 0

def set_device():
	o.device=get_device()
	if p.streaming==True:
		open_stream(p.url)
		p.stream.volume=config.appconfig['general']['volume']
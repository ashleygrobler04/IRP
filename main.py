import time
import sys
import config
import player
import wx
app = wx.App(redirect=False)
from gui import interface
config.setup()
interface.window.Show()

player.set_device()
if config.appconfig['general']['last']!="" and config.appconfig['general']['resumelast']==True:
	player.open_stream(config.appconfig['general']['last'])

app.MainLoop()
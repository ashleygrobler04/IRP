import speech
import config
from gui import options
from gui import streamopener
import os.path as path
import player
import application
import wx
class MainGui(wx.Frame):
	def __init__(self, title):
		wx.Frame.__init__(self, None, title=title, size=(350,200)) # initialize the wx frame
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)

		self.menuBar = wx.MenuBar()
		menu = wx.Menu()
		m_stream = menu.Append(-1, "Open Audio Stream\tControl-U", "")
		self.Bind(wx.EVT_MENU, self.stream, m_stream)
		m_options = menu.Append(-1, "Options...", "")
		self.Bind(wx.EVT_MENU, self.options, m_options)
		m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
		self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
		self.menuBar.Append(menu, "&File")
		menu = wx.Menu()
		m_play = menu.Append(-1, "Play/pause", "")
		self.Bind(wx.EVT_MENU, self.play, m_play)
		m_stop = menu.Append(-1, "Stop", "")
		self.Bind(wx.EVT_MENU, self.stop, m_stop)
		submenu = wx.Menu()
		m_volup = submenu.Append(-1, "Increase Volume\tControl Up arrow", "")
		self.Bind(wx.EVT_MENU, self.volup, m_volup)
		m_voldown = submenu.Append(-1, "Decrease Volume\tControl Down arrow", "")
		self.Bind(wx.EVT_MENU, self.voldown, m_voldown)
		menu.AppendMenu(wx.ID_ANY, "Volume", submenu)
		self.menuBar.Append(menu, "&Transport")
		self.SetMenuBar(self.menuBar)
		accel=[]
		accel.append((wx.ACCEL_CTRL, ord('U'), m_stream.GetId()))
		accel.append((wx.ACCEL_CTRL, ord('p'), m_play.GetId()))
		accel.append((wx.ACCEL_CTRL, ord('s'), m_stop.GetId()))
		accel.append((wx.ACCEL_CTRL, wx.WXK_UP, m_volup.GetId()))
		accel.append((wx.ACCEL_CTRL, wx.WXK_DOWN, m_voldown.GetId()))
		self.panel.Layout()
		accel_tbl=wx.AcceleratorTable(accel)
		self.SetAcceleratorTable(accel_tbl)

	def options(self,event):
		w=options.OptionsGui()
		w.Show()

	def stream(self,event):
		inp=streamopener.Input("Open Audio Stream","Enter a URL to an Audio Stream")
		inp.Show()

	def volup(self,event):
		if player.p.loaded==True:
			if player.p.stream.volume<1.0:
				try:
					player.p.stream.volume+=0.02
				except:
					pass
		config.appconfig['general']['volume']=round(player.p.stream.volume,2)
		config.appconfig.write()

	def voldown(self,event):
		if player.p.loaded==True:
			if player.p.stream.volume>0.0:
				try:
					player.p.stream.volume-=0.02
				except:
					pass
		config.appconfig['general']['volume']=round(player.p.stream.volume,1)
		config.appconfig.write()

	def play(self, event):
		if player.p.loaded==True and player.p.streaming==False:
			if player.p.stream.is_playing==False:
				player.play()
			else:
				player.pause()

	def stop(self, event):
		if player.p.loaded==True:
			if player.p.stream.is_playing==True:
				player.stop()

	def OnClose(self, event):
		"""App close event handler"""
		self.Destroy()
		config.appconfig.write()

global window
window=MainGui(application.name+" V"+application.version)
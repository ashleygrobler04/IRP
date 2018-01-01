import os, sys
import config
import wx
import player
class OptionsGui(wx.Frame):

	def __init__(self):

		self.ws=config.appconfig['general']['resumelast']
		wx.Frame.__init__(self, None, title="Options", size=(350,200)) # initialize the wx frame
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.last = wx.CheckBox(self.panel, -1, "&Resume last played item on startup")
		self.main_box.Add(self.last, 0, wx.ALL, 10)
		self.last.SetValue(self.ws)
		self.devices_label=wx.StaticText(self.panel, -1, "Audio Device")
		self.devices = wx.Choice(self.panel, -1)
		self.main_box.Add(self.devices, 0, wx.ALL, 10)
		devs=player.devices()
		for i in range(len(devs)):
			self.devices.Insert(devs[i],i)
		self.devices.SetSelection(player.get_device()-1)
		self.ok = wx.Button(self.panel, wx.ID_OK, "&OK")
		self.ok.Bind(wx.EVT_BUTTON, self.OnOK)
		self.main_box.Add(self.ok, 0, wx.ALL, 10)
		self.close = wx.Button(self.panel, wx.ID_CLOSE, "&Cancel")
		self.close.Bind(wx.EVT_BUTTON, self.OnClose)
		self.main_box.Add(self.close, 0, wx.ALL, 10)
		self.panel.Layout()

	def OnOK(self, event):
		config.appconfig['general']['resumelast']=self.last.GetValue()
		if config.appconfig['general']['device']!=self.devices.GetString(self.devices.GetSelection()):
			config.appconfig['general']['device']=self.devices.GetString(self.devices.GetSelection())
			player.set_device()
		config.appconfig.write()
		self.Destroy()

	def OnClose(self, event):
		self.Destroy()
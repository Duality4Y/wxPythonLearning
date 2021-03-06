import wx

class Frame(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id, "Duality's frame", size=(300,200))
		panel = wx.Panel(self)
		button = wx.Button(panel,label="exit",pos=(130,10),size=(60,60))
		self.Bind(wx.EVT_BUTTON, self.leaveFrame,button)
		self.Bind(wx.EVT_CLOSE, self.closewindow)
	def leaveFrame(self,event):
		self.Close(True)
	def closewindow(self,event):
		self.Destroy()
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = Frame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()

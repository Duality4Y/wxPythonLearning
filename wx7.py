import wx

class bucky(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,"title", size=(300,200))
		panel = wx.Panel(self)
		thing = wx.StaticText(panel, -1, "this is static text", (10,10))
		
		rev = wx.StaticText(panel, -1, "Static Text With Reversed Colors", (10, 30),(260,-1),wx.ALIGN_CENTER)
		rev.SetForegroundColour('blue')
		rev.SetBackgroundColour('red')
	

if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame = bucky(parent=None, id = -1)
	frame.Show()
	app.MainLoop()

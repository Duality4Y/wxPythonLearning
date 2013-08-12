import wx

class bucky(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Frame aka window', size = (300,200))
		panel = wx.Panel(self)
		
		wx.CheckBox(panel, -1, "Apples", (20,20), (160,-1))
		wx.CheckBox(panel, -1, "Tuna", (20, 40), (160, -1))
		wx.CheckBox(panel, -1, "RoastBeef", (20, 60), (160, -1))

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame=bucky(parent=None, id=-1)
	frame.Show()
	app.MainLoop()


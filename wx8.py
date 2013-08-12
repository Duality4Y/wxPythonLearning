import wx

class bucky(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'title', size=(300,200))
		panel = wx.Panel(self)
		
		test=wx.TextEntryDialog(None, "question?", 'title', 'enter name')
		if test.ShowModal() == wx.ID_OK:
			apples = test.GetValue()
		
		wx.StaticText(panel, -1, apples, (30,30))
	


if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame=bucky(parent=None, id=-1)
	frame.Show()
	app.MainLoop()

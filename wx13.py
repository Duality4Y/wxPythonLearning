import wx

class bucky(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Frame aka window', size = (300,200))
		panel = wx.Panel(self)
		
		mylist = ['beef', 'tuna', 'coconuts', 'more beef', 'cereal']
		cont = wx.ListBox(panel, -1, (20,20), (100,80), mylist, wx.LB_SINGLE)
		cont.SetSelection(3)

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame=bucky(parent=None, id=-1)
	frame.Show()
	app.MainLoop()


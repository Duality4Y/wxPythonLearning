import wx

class bucky(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self,parent,id,'a frame', size=(300,300))
		panel = wx.Panel(self)
		
		status = self.CreateStatusBar()
		
		menuBar = wx.MenuBar()
		
		first = wx.Menu()
		second = wx.Menu()
		
		first.Append(wx.NewId(), 'New Window', 'This creates a new window')
		first.Append(wx.NewId(), 'Open ', 'opens an file')
		
		menuBar.Append(first,"File")
		menuBar.Append(second,"Edit")
		self.SetMenuBar(menuBar)

if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame=bucky(parent=None,id=-1)
	frame.Show()
	app.MainLoop()

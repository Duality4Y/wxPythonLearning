import wx
class bucky(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self,parent,id,"Frame aka window", size=(300,200))
		panel = wx.Panel(self)
		
		box = wx.MessageDialog(None,'Do I have the best tuts?','title',wx.OK)
		answer = box.ShowModal()
		print answer
		box.Destroy()

if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = bucky(parent=None,id=-1)
	frame.Show()
	app.MainLoop()

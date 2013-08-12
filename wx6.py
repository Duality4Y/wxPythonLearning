import wx

class bucky(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'title',size=(300,200))
		panel = wx.Panel(self)
		
		box = wx.SingleChoiceDialog(None,'Question?','title',['Tuna','second option','third option'])
		if box.ShowModal()==wx.ID_OK:
			answer = box.GetStringSelection()
		print "answer: ",answer

if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = bucky(parent=None, id = -1)
	frame.Show()
	app.MainLoop()

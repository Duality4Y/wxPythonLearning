import wx

if __name__ == '__main__':
	app = wx.PySimpleApp()
	
	names = ['Robert','misty','astrid','adriaan']
	modal = wx.SingleChoiceDialog(None, "What's your name", "Title", names)
	if modal.ShowModal() == wx.ID_OK:
		print "your name is: ", modal.GetStringSelection()
	modal.Destroy()

"""
	github.com/duality4y
"""

import wx
from wxSDLWindow import wxSDLWindow
import pygame

#class for doing frame and pygame things.

class MyFrame(wxSDLWindow):
	def process(self):
		print "processes"
	def InitUI(self):
		pass
	def draw(self):
		pass

def main():
	app = wx.PySimpleApp()
	screen_size = (640, 480)
	frame = MyFrame(None, -1, title='SDL window', size=screen_size)
	wincow.Show(1)
	app.MainLoop()

if __name__ == '__main__':
	main()


"""
	github.com/duality4y
	
"""
import wx
from wxSDLWindow import wxSDLWindow
import pygame

#class for drawing a circle in a wxPythonPygame window

class CircleWindow(wxSDLWindow):
	def process(self):
		pass
	def InitUI(self):
		pass
	#define a drawing function
	def draw(self):
		surface = self.getSurface()
		if surface is not None:
			topcolor = 5
			bottomcolor = 100
			
			pygame.draw.circle(surface, (250, 0, 0), (100, 100), 50)
			
			pygame.display.flip()

def main():
	app = wx.PySimpleApp()
	screen_size = (640, 480)
	window = CircleWindow(None, -1, title = 'sdl window', size=screen_size)
	window.Show(1)
	app.MainLoop()

if __name__ == "__main__":
	main()

#
# pykarel by Daniel Johnson <ComputerDruid@gmail.com>
#
import Tkinter
import threading
from time import sleep
WIDTH=600
HEIGHT=600
speed=5
numRows=10
numCols=10
blockWidth=WIDTH/numCols
blockHeight=HEIGHT/numRows
robots = []
karelimages = []

def __initGraphics():
	global hlines,vlines
	hlines=[]
	for i in xrange(0,numRows):
		hlines.append(w.create_line(0,i*blockHeight+blockHeight/2,WIDTH,i*blockHeight+blockHeight/2,fill="red"));
	vlines=[]
	for i in xrange(0,numCols):
		vlines.append(w.create_line(i*blockWidth+blockWidth/2,0,i*blockWidth+blockWidth/2,HEIGHT,fill="red"));

def keepWindowOpen():
	pass
	#rootW.mainloop()

def step():
	sleep(2-speed/5.0)

def addRobot(r):
	robots.append(r)

class robot:
	def __init__(self):
		addRobot(self)
		self.x=1
		self.y=1
		self.direction=0
		self.image=w.create_image(self.x*blockWidth+blockWidth/2, self.y*blockHeight+blockHeight/2, image=karelimages[0])
		step()
	def move(self):
		if self.direction == 0:
			self.x+=1
		self.draw()
		step()
	def draw(self):
		w.coords(self.image,self.x*blockWidth+blockWidth/2, self.y*blockHeight+blockHeight/2)


rootW = Tkinter.Tk()

w = Tkinter.Canvas(rootW,width=WIDTH,height=HEIGHT,background="white")
w.pack()
__initGraphics()
karelimages.append(Tkinter.PhotoImage(file = 'karele.gif'))
karelimages.append(Tkinter.PhotoImage(file = 'kareln.gif'))
karelimages.append(Tkinter.PhotoImage(file = 'karelw.gif'))
karelimages.append(Tkinter.PhotoImage(file = 'karels.gif'))
threading.Thread(target=rootW.mainloop).start()

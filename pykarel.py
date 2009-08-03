#
# pykarel by Daniel Johnson <2010djohnson@tjhsst.edu>
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
local=threading.local()
robots = []
beepers = []

def __initGraphics():
	global hlines,vlines
	hlines=[]
	for i in xrange(0,numRows):
		hlines.append(w.create_line(0,i*blockHeight+blockHeight/2,WIDTH,i*blockHeight+blockHeight/2,fill="red"));
	vlines=[]
	for i in xrange(0,numCols):
		vlines.append(w.create_line(i*blockWidth+blockWidth/2,0,i*blockWidth+blockWidth/2,HEIGHT,fill="red"));

def __windowkilled():
	print "window deleted"
	rootW.destroy()

def __init():
	global rootW,w
	rootW = Tkinter.Tk()
	rootW.protocol("WM_DELETE_WINDW", __windowkilled)
	
	w = Tkinter.Canvas(rootW,width=WIDTH,height=HEIGHT,background="white")
	w.pack()
	__initGraphics()
	local.karelimages = []
	local.karelimages.append(Tkinter.PhotoImage(file = 'karele.gif'))
	local.karelimages.append(Tkinter.PhotoImage(file = 'kareln.gif'))
	local.karelimages.append(Tkinter.PhotoImage(file = 'karelw.gif'))
	local.karelimages.append(Tkinter.PhotoImage(file = 'karels.gif'))
	w.after(10,__update)
	rootW.mainloop()
	
def __update():
	#print "__update() called"
	for r in robots:
		r.draw()
	w.after(100,__update)

def setSpeed(s):
	global speed
	speed=s
	if s>10:
		speed=10
	elif s<1:
		speed=1

def step():
	sleep(2-(speed-1)/5.0)

def addRobot(r):
	robots.append(r)

class beeperPile:
	def __init__(self):
		self.count=1
		self.x=1
		self.y=1

def addBeeper(x,y):
	for s in beepers:
		if s.x==x and s.y ==y:
			s.beepers+=1
			return
	#else
	b=beeperPile()
	b.x=x
	b.y=y
	beepers.append(b)

class robot:
	def __init__(self):
		addRobot(self)
		self.x=1
		self.y=1
		self.direction=0
		self.beepers=0
		step()
	def move(self):
		if self.direction == 0:
			self.x+=1
		elif self.direction == 1:
			self.y-=1
		elif self.direction == 2:
			self.x-=1
		else:
			self.y+=1
		step()
	def putBeeper(self):
		if self.beepers>0:
			self.beepers-=1
			addBeeper(x,y)
	def turnLeft(self):
		self.direction=(self.direction+1)%4
		step()
	def draw(self):
		#try:
		#	w.coords(self.image,self.x*blockWidth+blockWidth/2, self.y*blockHeight+blockHeight/2)
		#except AttributeError:
		try:
			w.delete(self.image)
		except AttributeError:
			pass
		self.image=w.create_image(self.x*blockWidth+blockWidth/2, self.y*blockHeight+blockHeight/2, image=local.karelimages[self.direction])


threading.Thread(target=__init).start()

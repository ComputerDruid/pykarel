#
# pykarel by Daniel Johnson <ComputerDruid@gmail.com>
#
import Tkinter
from time import sleep
WIDTH=800
HEIGHT=800
speed=5
numRows=10
numCols=10
blockWidth=WIDTH/numCols
blockHeight=HEIGHT/numRows

def __initGraphics():
	global hlines,vlines
	hlines=[]
	for i in xrange(0,numRows):
		hlines.append(w.create_line(0,i*blockHeight+blockHeight/2,WIDTH,i*blockHeight+blockHeight/2,fill="red"));
	vlines=[]
	for i in xrange(0,numCols):
		vlines.append(w.create_line(i*blockWidth+blockWidth/2,0,i*blockWidth+blockWidth/2,HEIGHT,fill="red"));

def keepWindowOpen():
	rootW.mainloop()

def step():
	sleep(2-speed/5.0)

rootW = Tkinter.Tk()

w = Tkinter.Canvas(rootW,width=WIDTH,height=HEIGHT,background="white")
w.pack()
__initGraphics()
keepWindowOpen()

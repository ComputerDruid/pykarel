import pykarel
pykarel.setSpeed(10)
r = pykarel.robot()
r.move()
r.move()
p = pykarel.robot()
p.move()
p.turnLeft()
p.turnLeft()
p.turnLeft()
p.move()
for i in xrange(40):
	p.move()
	p.turnLeft()
print "lab done"

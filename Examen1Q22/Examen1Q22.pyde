import random

def sparkle():
    line(x,y,b,y)

def setup():
    background(0)
    size(400,400)
    stroke(255)


def draw():
  for i in range(90):
    pushMatrix()
    x= map(random.random(), 0,1,1,400)
    y= map(random.random(), 0,1,1,400)
    b= map(random.random(), 0,1,1,400) 
    line(x,y,x-b,y)
#    translate(x,y)
#    sz= map(random.random(), 0,1,0.5,1)
#    scale(sz,sz)
#    sparkle()
    popMatrix()
    noLoop()
    

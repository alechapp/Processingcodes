import random

def sparkle():
    rotate(75*PI/100.0)
    fill(255)
    rect(30,30,30,30)

def setup():
    background(255)
    size(500,500)
    fill(0,64,0)
    triangle(250,50,50,450,450,450)

def draw():
  col2 = -3355444
  for i in range(50):
    pushMatrix()
    x= map(random.random(), 0,1,250,450)
    y= map(random.random(), 0,1,250,450)
    if get(int(x), int(y)) == col2:
        continue
    translate(x,y)
    sz= map(random.random(), 0,1,0.5,1)
    scale(sz,sz)
    sparkle()
    popMatrix()
    noLoop()
    
    

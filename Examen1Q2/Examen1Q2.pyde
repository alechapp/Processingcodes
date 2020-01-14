import random

def draw_slash(x,y,b) :
     line(y, x, y, x+b)

def setup() :
    size    (400,400)
    
def draw() :
 background(0,0,0)
 stroke(169,169,169)
 random(1,40)
 for j in range(90) :
  for i in range(50) :
    draw_slash(random.random()* j, random.random() * i, random.random())
    noLoop()

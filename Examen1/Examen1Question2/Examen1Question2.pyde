import random
def draw_angle(left, hauteur):
    line(left, hauteur, left + map(random.random(),0,1,0,20), hauteur)

def setup():
    size(400,400)

def draw():
    background(0)
    stroke(169)
    for i in range(120):
     rvar = random.random()
     draw_angle(random.random()*width, map(rvar,0,1,1,400))
     noLoop()

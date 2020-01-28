import random
def draw_angle(left, top, bottom):
    line(left, top, left + bottom, top)
    line(left, top, left, top + bottom)


def setup():
    size(900,900)

def draw():
    background(0)
    for i in range(80):
     rvar = random.random()
     stroke(map(rvar,0,1,255,0))
     draw_angle(random.random()*width,random.random()*height, map(rvar,0,1,90,100))
     noLoop()

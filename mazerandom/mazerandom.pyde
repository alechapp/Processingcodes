import random

char_width = 20
def draw_slash(b, x, y) :
 if b < 0.5 :
     line(y + char_width, x + (char_width / 2), y, x+ (char_width / 2))
 else :
     line(y+ (char_width / 2), x, y+ (char_width / 2), x + char_width)

     

def setup() :
    size    (400,400)
    
def draw() :
 for j in range(20) :
  for i in range(20) :
    draw_slash(random.random(), char_width * j, char_width * i)
    noLoop()
    saveFrame("mazerandom.png")

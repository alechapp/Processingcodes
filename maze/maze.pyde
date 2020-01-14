import random

char_width = 20
def draw_slash(fwd_slash, x, y) :
 if fwd_slash :
     line(y + char_width, x, y, x + char_width)
 else :
     line(y, x, y + char_width, x + char_width)

def setup() :
    size    (400,400)
    
def draw() :
 for j in range(height / char_width) :
  for i in range(width / char_width) :
    draw_slash(False, char_width * j, char_width * i)
    draw_slash(True, char_width * j, char_width * i)

    noLoop
    

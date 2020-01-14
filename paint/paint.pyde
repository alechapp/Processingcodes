stroke_width = 5

def setup():
 size(900,900)
 background(255)

def draw():
    global stroke_width
    delta = 0.5
    if keyPressed :
       if keyCode == UP :
          stroke_width= stroke_width + delta
       if keyCode == DOWN :
          stroke_width= stroke_width - delta
          
    if stroke_width < 1 :
        stroke_width = 1
          
    strokeWeight(stroke_width)
          
    if mousePressed :
      if mouseButton == LEFT :
        stroke(0)
      if mouseButton == RIGHT :
        stroke(255,102,189)
      if mouseButton == CENTER :
        stroke(102,155,255)  
      line(pmouseX, pmouseY, mouseX, mouseY)
      

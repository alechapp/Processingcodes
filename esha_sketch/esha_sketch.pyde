delta = 5
x=450
y=450

def setup():
 size(900,900)
 background(128)

def draw():
    global delta
    global x, y
    
    strokeWeight(5)
         
    px = x
    py = y
           
    line(x,y,x,y)
    if keyPressed :
       if keyCode == UP :
          y = y - delta
       if keyCode == DOWN :
          y = y + delta
       if keyCode == LEFT :
          x = x - delta
       if keyCode == RIGHT :
          x = x + delta
     
    if x > 900 :
         x = 900
    if x < 0 :
         x = 1
    if y < 0 :
         y = 1
    if y > 900 :
         y = 900
         
    line(x, y, px, py)
    
    if key == " " :
        background(128)  
    

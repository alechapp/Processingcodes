y=200
delta=10
def setup():
    size(400,400)
    
def draw():
    background(0,0,0)
    stroke(255,255,255)
    global delta
    global y
    
    line(80,y,100,y-10)
    line(80,y-20,100,y-10)   
    if keyPressed: 
        if key == 'w':
            y = y - delta
    if keyPressed: 
        if key == 's':
            y = y + delta
            
    if y > 400:
        y = 400
    if y < 0:
        y = 20
noLoop

    

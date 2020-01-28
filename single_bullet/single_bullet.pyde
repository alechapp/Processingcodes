y=200
deadtime=0

def setup():
    global xs
    xs=[]
    size(400,400)
    stroke(0)
    
def draw():
    global xs, deadtime, y
    
    strokeWeight(5)
    background(169)
    
    if keyPressed and key == " " and deadtime <=0:
        xs.append(0)
        deadtime=10
    deadtime -= 1     
    
    if keyPressed and key== 'w' :
        y= y+10
    if keyPressed and key== 's' :
        y=y-10
         
    for i in range(len(xs)):
        x=xs[i]
        line(x,y,x+20,y)
        x=x+10
        xs[i]=x
            
    if len(xs) > 0 and xs[0] > width:
      xs.pop(0)
    print(xs)
        

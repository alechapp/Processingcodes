def setup():
    size(480,480)
    
def draw():
    rect_width = 100
    fill(0,0,0)
    stroke(250,250,250)
    rect(50, 20, rect_width, rect_width)
    
    fill(50, 179, 123)
    stroke(0,0,0)
    ellipse(85,50,20,20)
    ellipse(115,50,20,20)
    
    stroke(250,250,250)
    line(50,20,100,100)
    line(150,20,100,100)

saveframe("squarefox")
noloop

    

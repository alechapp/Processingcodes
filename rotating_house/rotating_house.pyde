def house():
    triangle(15, 0, 0, 15, 30, 15)
    rect(0,15,30,30)
    rect(12,30,10,15)
    
def setup():
    size(900,900)
    
def draw():
    #background(128)
    pushMatrix()
    translate(350,350)
    rotate(frameCount * PI/200.0)
    for j in range(1):
     for i in range(1):
         pushMatrix()
         translate(+i*50, +j *100)
         rotate(-frameCount * PI/50.0)
         translate(frameCount*.5,0)
         house()
         popMatrix()
         
    popMatrix()

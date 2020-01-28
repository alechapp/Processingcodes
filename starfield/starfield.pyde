import random

def setup():
    global star_x, star_y, shade
    star_x=[]
    star_y=[]
    shade=[]
    for i in range(100):
        star_x.append(400*random.random())
        star_y.append(400*random.random())
    size(400,400)
    
    
def draw():
    background(128)
    fill(255)
    global star_x, star_y
    for i in range(len(star_x)):
        star_y[i] += 1 + random.random() * 2
        if star_y[i] > width:
            star_y[i] = 0
            star_x[i] = random.random()*height     
        circle(star_x[i], star_y[i], 30)
    if frameCount %15 ==0:
       if len(star_x)==0
          down_to_zero=True
       if down_to_zero=False:
          star_x.pop(-1)
          star_y.pop(-1)
       else:
           star_x
        

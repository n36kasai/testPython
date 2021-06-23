list_x = []
list_y = []

def sampleDraw(col):
    stroke(col)
    line(300, 0, 300, 600)
    line(0, 300, 600, 300)

def setup():
    size(600, 600)
    global list_X, list_y
    for i in range(0,9):
        list_x.append(mouseX)
        list_y.append(mouseY)

def draw():
    background(100)
    sampleDraw(255)
    
    for i in range(0, 9):
        fill(i * 20)
        ellipse(list_x[i], list_y[i], 30, 30)
    
    fill(255)    
    ellipse(mouseX, mouseY, 30, 30)
    
    del list_x[0]
    del list_y[0]
    list_x.append(mouseX)
    list_y.append(mouseY)

def sampleDraw(col):
    stroke(col)
    line(300, 0, 300, 600)
    line(0, 300, 600, 300)

def setup():
    size(600, 600)

def draw():
    sampleDraw(255)

#Aaron Cheng
#Controls:
    # l: turn on and off leaves
    # n: turn on an off numbering
    # a: tilt the branches left
    # d: tilt the branches right
    # w: increase the branches', numbers', and leaves' sizes
    # d: decrease the branches', numbers', and leaves' sizes
    # click: toggle animation for the tree to sway "naturally"
    # z: increase number of branches
    # x: decrease number of branches
    # c: change leaf and number colors to a random color
import sys
import random
import math


def setup():
    size(1100, 800)
    background(255)
    pixelDensity(displayDensity())

def drawLineAngle(color, start, angle, length, width=1):
    angle += 180  # make up zero degrees
    end = (start[0] + math.sin(math.radians(angle)) * length,
           start[1] + math.cos(math.radians(angle)) * length)
    stroke(*color)
    if width:
        strokeWeight(width)
    else:
        noStroke()
    line(*(start + end))
    return end

def drawLeaf(location):
    global treeWidth, leafColor
    stroke(0, 50, 0)
    fill(*leafColor)
    strokeWeight(0.5)
    ellipse(location[0],location[1],5+treeWidth/5,5+treeWidth/5)
        
def drawNumber(location):
    global number, treeWidth, leafColor
    stroke(0, 50, 0)
    fill(*leafColorc)
    strokeWeight(0.5)
    ellipse(location[0],location[1],18+treeWidth/5,18+treeWidth/5)
    textSize(13+treeWidth/5)
    textAlign(CENTER)
    fill(0,0,0)
    text(number,location[0],location[1]+5+treeWidth/10)
    number+=1
    

def drawTree(start,leaf,showNumber,angle,count,length,width):
    global tilt, depth
    end = drawLineAngle((0,0,0),start,angle,length,width)
    
    if count < depth:
        drawTree(end,leaf,showNumber,angle+(30-count/2)+tilt,count+1,length/1.2,width/1.4)
        drawTree(end,leaf,showNumber,angle-(30-count/2)+tilt,count+1,length/1.2,width/1.4)
    elif leaf:
        drawLeaf(end)
    if showNumber:    
        drawNumber(end)

def mouseClicked():
    global animate, tilt
    animate = not animate
    if not animate:
        tilt = 0
def keyPressed():
    global leaf, showNumber, tilt, treeWidth, animate, depth, leafColor
    if key=="l":
        leaf = not leaf
    if key=="n":
        showNumber = not showNumber
    if key=="a" and not animate:
        tilt += 10
    if key=="d" and not animate:
        tilt -= 10
    if key=="w":
        treeWidth += 10
    if key=="s":
        treeWidth -= 10
    if key=="z":
        if depth < 20:
            depth += 1
    if key=="x":
        if depth > 1:
            depth -= 1
    if key=="c":
        leafColor = [random.random()*255 for i in range(3)]

def setup():
    global leaf, showNumber, treeWidth, tilt, animate, depth, leafColor
    leaf, showNumber, animate = True, True, False
    tilt, treeWidth, counter, depth = 0, 0, 0, 5
    leafColor = [100,255,100]

def draw():
    global number, treeWidth, tilt, counter
    number=0
    #animation = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
    #             -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    animation = [0.25] * 16 + [-0.25] * 32 + [0.25] * 16
    clear()
    background(255)
    if treeWidth <= 0:
        treeWidth=0
    if animate:
        tilt += animation[counter%64]
        counter += 1
    else:
        counter = 0
    drawTree((550,800),leaf,showNumber,0,0,150,20+treeWidth)
#Aaron Cheng

import turtle
import math
import random

def drawPlanet(center, size, color, orbitRadius, angle):
    location=[x+orbitRadius*f(angle)
              for x,f in zip(center, (math.sin, math.cos))]
    turtle.penup()
    turtle.goto(*location)
    turtle.dot(size*2,color)

class Sun:
    def __init__(self,center,size,color):
        self.center = center
        self.size = size
        self.color = color
        self.turtle = turtle.Turtle()
        self.orbitRadius = 0
        self.speed = 0
        self.type = "sun"
    def draw(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(self.center[0], self.center[1])
        self.turtle.dot(self.size, self.color)
    def setColor(self, color):
        self.color = color
    def inside(self, location):
        distance = math.sqrt(math.pow(location[0]-self.center[0], 2) + math.pow(location[1]-self.center[1], 2))
        return distance <= (self.size * math.pi)
    def onClick(self, location):
        if (self.inside(location)):
            self.setColor(randomColor())
            return True
        else:
            return False
    def onKey(self, key):
        if key == 0:
            self.size += 10
        elif key == 1:
            self.size -= 10
        elif key == 2:
            self.orbitRadius -= 50
        elif key == 3:
            self.orbitRadius += 50
        elif key == 4:
            self.speed -= .01
        elif key == 5:
            self.speed += .01
        elif key == 6:
            self.setColor(randomColor())

class Planet(Sun):
    def __init__(self, orbitAround, orbitRadius, size, color, speed, type):
        self.orbitAround = orbitAround
        super().__init__(self.orbitAround.center, size, color)
        self.orbitRadius = orbitRadius
        self.speed = speed
        self.size *= 2
        self.randomAngle = random.random()
        self.type = type

    def move(self):
        self.center=[x+self.orbitRadius*f(self.randomAngle)
                  for x,f in zip(self.orbitAround.center, (math.sin, math.cos))]
        self.randomAngle += self.speed

def randomColor():
    return [random.random() for i in range(3)]

class SolarSystem:
    def __init__(self):
        self.sun = Sun((0,0), 100, "yellow")
        self.planets = [Planet(self.sun,(i+1)*500,random.random()*50,randomColor(),random.random()*.01, "planet")
                        for i in range(random.randint(1,10))]
        self.moons = []
        for planet in self.planets:
            for i in range(random.randint(1,2)):
                self.moons.append(Planet(planet, 200, random.random()*10, randomColor(), random.random()*.1, "moon"))
        self.clicked = []
    def draw(self):
        self.sun.draw()
        for planet in self.planets:
            planet.move()
            planet.draw()
        for moon in self.moons:
            moon.move()
            moon.draw()

    def onClick(self, coords):
        self.clicked = []
        if self.sun.onClick(coords):
            self.clicked.append(self.sun)
        for planet in self.planets:
            if planet.onClick(coords):
                self.clicked.append(planet)
        for moon in self.moons:
            if moon.onClick(coords):
                self.clicked.append(moon)

    def onKey(self, key):
        for clicked in self.clicked:
            clicked.onKey(key)

    def keyN(self):
        for clicked in self.clicked:
            if clicked.type == "sun":
                self.planets.append(Planet(clicked,500,random.random()*50,randomColor(),random.random()*.01, "planet"))
            else:
                self.moons.append(Planet(clicked, 200, random.random()*10, randomColor(), random.random()*.1, "moon"))

def draw():
    turtle.clear()
    turtle.tracer(0,0)
    turtle.penup()
    turtle.goto(0,0)
    #sun.draw()
    #planet.move()
    #planet.draw()
    solarSystem.draw()
    global angle
    angle+=0.01
    screen.ontimer(draw,0)

def onClick(x,y):
    solarSystem.onClick((x,y))

def keyRight():
    solarSystem.onKey(3)

def keyUp():
    solarSystem.onKey(0)

def keyDown():
    solarSystem.onKey(1)

def keyLeft():
    solarSystem.onKey(2)

def keySpace():
    solarSystem.onKey(6)

def keyLeftBracket():
    solarSystem.onKey(4)

def keyRightBracket():
    solarSystem.onKey(5)

def keyN():
    solarSystem.keyN()

angle = 0
#sun=Sun((0,0), 30, "yellow")
#planet=Planet(sun,200,50,"Blue",0.01)
solarSystem=SolarSystem()
turtle.setworldcoordinates(-2000,-2000,2000,2000)
turtle.tracer(0,0)
turtle.ht()
screen=turtle.Screen()
screen.onkey(turtle.bye, "q")
screen.ontimer(draw,0)
screen.onclick(onClick)
screen.onkey(keyUp, "Up")
screen.onkey(keyDown, "Down")
screen.onkey(keyLeft, "Left")
screen.onkey(keyRight, "Right")
screen.onkey(keySpace, "space")
screen.onkey(keyLeftBracket, "bracketleft")
screen.onkey(keyRightBracket, "bracketright")
screen.onkey(keyN, "n")
screen.listen()
screen.mainloop()

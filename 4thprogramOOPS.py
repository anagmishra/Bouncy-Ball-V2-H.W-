import pgzrun
from random import randint

#Constants
TITLE="Bouncy Ball"
HEIGHT=500
WIDTH=500
GRAVITY=2000
CLR=0
CLR1=0
CLR2=0
CLR3=0
CLR4=0
class Ball:
    def __init__(self, x, y, ra, r, g, b):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.uy = 0
        self.r = r
        self.g = g
        self.b = b
        self.radius = ra
        self.CLR = (r, g, b)

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius,self.CLR)

    def update(self, dt): #dt is fps
        #Applying the constant acceleration formulae
        self.uy = self.vy
        self.vy += GRAVITY*dt
        self.y += (self.uy + self.vy)*0.5*dt

        #Detecting and handling the bounce
        if self.y>HEIGHT-self.radius:
            self.y = HEIGHT-self.radius
            self.vy = -self.vy*0.9 #Inelastic collision

        # X component does not have acceleration but it has constant velocity
        self.x += self.vx*dt
        if self.x>WIDTH - self.radius or self.x<self.radius:
            self.vx = -self.vx

bouncy_ball= Ball(25, 25, 30, 200, 200, 100)
bouncy_ball1= Ball(300, 100, 40, 183, 0, 10)
bouncy_ball2= Ball(250, 300, 50, 0, 200, 168)
bouncy_ball3= Ball(450, 45, 60, 255, 200, 100)
bouncy_ball4= Ball(460, 97, 70, 200, 255, 100)

def draw():
    screen.clear()
    bouncy_ball.draw()
    bouncy_ball1.draw()
    bouncy_ball2.draw()
    bouncy_ball3.draw()
    bouncy_ball4.draw()

def update(dt):
    bouncy_ball.update(dt)
    bouncy_ball1.update(dt)
    bouncy_ball2.update(dt)
    bouncy_ball3.update(dt)
    bouncy_ball4.update(dt)

def on_key_down(key):
    if key == keys.SPACE:
        bouncy_ball.vy = -500
        bouncy_ball1.vy = -400
        bouncy_ball2.vy = -350
        bouncy_ball3.vy = -200
        bouncy_ball4.vy = -700
        

pgzrun.go()
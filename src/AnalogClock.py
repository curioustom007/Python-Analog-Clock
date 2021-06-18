import math
import pyglet
import numpy as np
from pyglet.gl import *
from time import time, strftime, localtime
from datetime import datetime

win = pyglet.window.Window(fullscreen=False)

width = win.width
height = win.height


def PointsInCircum(r, n, pi=math.pi):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

def drawHourPoints(pts):
    hour = 1
    for i in pts[1:]:
        pyglet.text.Label(str(hour),
                          font_name='Ariel',
                          font_size=10,
                          x=i[1]+width//2, y=i[0]+height//2,
                          anchor_x='center', anchor_y='center',color=(136,206,235,255)).draw()
        hour += 1

def drawSecondPoints(pts):
    for i in pts:
        glBegin(GL_POINTS)
        glVertex3f(width//2,height//2,0)
        glVertex3f(i[1]+width//2,i[0]+height//2,0)
        glEnd()

def calculatePoints(x1,y1,d):
    angle = math.atan(y1/x1)
    hypo = y1/math.sin(angle)
    if x1 < 0:
        hypo = hypo - d
    else:
        hypo = hypo + d
    q = hypo * math.sin(angle)
    p = hypo * math.cos(angle)
    return p,q

def drawMillisecondPoints(pts):
    glBegin(GL_POINTS)
    for i in pts[:]:
        glVertex3f(i[1]+width//2, i[0]+height//2-50, 0)
    glEnd()

secondPoints = np.array(PointsInCircum(110,6000))
hourPoints = np.array(PointsInCircum(40,60))
minutPoints = np.array(PointsInCircum(95,3600))
hourDigits = np.array(PointsInCircum(100,12))
millisecondPoints = np.array(PointsInCircum(15,100))
millisecond12Points = np.array(PointsInCircum(15,12))
#secondPoints = np.array(PointsInCircum(100,60))


dt = datetime.now()

second = dt.second
hour = dt.hour
minute = dt.minute
milisecondHandMovement = dt.microsecond//10000
secondHandMovement = (second * 100) + (milisecondHandMovement)
minuteHandMovement = (minute * 60) + (second)


def update_frame(x, y):
    global second
    global hour
    global minute
    global secondHandMovement
    global dt
    global minuteHandMovement
    global milisecondHandMovement
    dt = datetime.now()
    second = dt.second
    hour = dt.hour if dt.hour <= 12 else dt.hour%12
    minute = dt.minute
    milisecondHandMovement = dt.microsecond//10000
    secondHandMovement = (second * 100) + (milisecondHandMovement)
    minuteHandMovement = (minute * 60) + (second)

glColorMask(1,1,1,1)

@win.event
def on_draw():
    # clear the screen
    glClear(GL_COLOR_BUFFER_BIT)

    # drawSecondPoints(secondPoints)

    drawHourPoints(hourDigits)
    
    drawMillisecondPoints(millisecond12Points)
    
    glLineWidth(2)
    
    x = width//2
    y = height//2
    x1 = secondPoints[secondHandMovement][1]+x
    y1 = secondPoints[secondHandMovement][0]+y
    p, q = calculatePoints(x1-x,y1-y,10)
    p += x
    q += y
    glBegin(GL_LINES)    
    glVertex3f(p, q, 0)
    glVertex3f(x1, y1, 0)
    glEnd()
    
    

    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex3f(x,y,0)
    glVertex3f(minutPoints[minuteHandMovement][1]+x,minutPoints[minuteHandMovement][0]+y,0)
    glEnd()

    glLineWidth(1.5)
    glBegin(GL_LINES)
    glVertex3f(x,y,0)
    glVertex3f(hourPoints[(hour*5)+(minute//12)][1]+x,hourPoints[(hour*5)+(minute//12)][0]+y,0)
    glEnd()
    
    x = width//2
    y = height//2-50
    x1 = millisecondPoints[milisecondHandMovement][1]+x
    y1 = millisecondPoints[milisecondHandMovement][0]+y
    glBegin(GL_LINES)    
    glVertex3f(x, y, 0)
    glVertex3f(x1, y1, 0)
    glEnd()

pyglet.clock.schedule(update_frame, 1)
pyglet.app.run()

import sys
import math
import OpenGL

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

particles = []
pointx = 0
pointy = 0

def main():
    pointx = input('position.x for the test point: ')
    pointx = int(pointx)
    pointy = input('position.y for the test point: ')
    pointy = int(pointy)
    
    n = input('particle count: ')
    n = int(n)
    
    for i in range(n):
        x = input('position.x for ' + str(i) + ': ')
        q = input('charge for ' + str(i) + ': ')

        particles.append((int(x), int(q)))

    print particles

    #sort particles by distance from origin
    particles.sort(key=lambda x: x[0])

    print particles[-1:][0][0]
    print compute_field()
    
    glutInit(len(sys.argv), sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800,640)
    glutCreateWindow('Electro')

    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_ALPHA_TEST)
    glutDisplayFunc(display)

    glViewport(0, 0, 800, 640)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 640)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
     

    render_grid()
    plot_field()
    plot_charges()
    
    glutSwapBuffers()
    return

def compute_field():
    E = 0
    for x, q in particles:
        vector1 = (pointx, pointy)
        vector2 = (x, 0)
        #compute dot product
        a = sum(p*q for p, q in zip(vector1, vector2))
        #total field = sum (cos alpha)(y - yi)
        E = E + (a * pointy)
    return E

def plot_charges():
    glColor4f(1, 1, 0, 1)
    #get the farest particle to bound the system to the window
    boundingx = 600 / particles[-1:][0][0]

    print boundingx
    
    for x, q in particles:
        glPointSize(q + 4)
        glBegin(GL_POINTS)

        glVertex3f((x * boundingx) + 100, 100, -0.1)
        print x * boundingx
        
        glEnd()
    return

#Not finished
def plot_field():
    glBegin(GL_LINES)

    glColor4f(.2, .2, .2, .51)
    
    #Needs to implemet rotations on x
    for x in range(0, 850, 25):
        for y in range(0, 650, 25):
            glVertex2f(x+12, y+5)
            glVertex2f(x+12, y+20)

            glVertex2f(x+9, y+17)
            glVertex2f(x+12, y+20)

            glVertex2f(x+15, y+17)
            glVertex2f(x+12, y+20)
        
    glEnd()
    return

def render_grid():
    glDisable(GL_LINE_SMOOTH)
    glBegin(GL_LINES)

    #Draw axis
    glColor4f(1, 0, 0, 1)
    glVertex2f(100.0,100.0)
    glVertex2f(700.0,100.0)

    glColor4f(0, 0, 1, 1)
    glVertex2f(100.0,100.0)
    glVertex2f(100.0,540.0)
    
    glColor4f(0, .21, 0, 1)
    for i in range(25, 850, 25):
        glVertex2f(i,0.0)
        glVertex2f(i,640.0)

        glVertex2f(0.0,i)
        glVertex2f(800.0,i)
        
    glEnd()
    glEnable(GL_LINE_SMOOTH)
    return

if __name__ == '__main__': main()

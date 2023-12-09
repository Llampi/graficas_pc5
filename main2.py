import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import *
import random

posiciones = []

for i in range(50):
    posiciones.append([random.uniform(-25, 25),random.uniform(-17, 17)])

def main():
    
    pygame.init()
    display = (1000,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-10)
 



    obj = OBJ('model/texto.obj', swapyz=True)
    

    glPushMatrix()

    glCallList(obj.gl_list)


    arbol = OBJ('model/arbol.obj', swapyz=True)

    glCallList(arbol.gl_list)

    glPopMatrix()

    glPushMatrix()

    estrella = OBJ('model/estrella.obj', swapyz=True)
    glCallList(estrella.gl_list)
    glPopMatrix()
    


    angle = 0.0  
    speed = 1.0 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glColor3f(1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

 

        glPushMatrix()
        glTranslatef(9.0,2.0,-10)
        glRotatef(-90, 1.0, 0.0, 0.0) 
        glRotatef(angle, 0.0, 0.0, 1.0)  
        glCallList(arbol.gl_list)
        glPopMatrix()



        glPushMatrix()
        glTranslatef(-9.0,2.0,-10)
        glRotatef(-90, 1.0, 0.0, 0.0) 
        glRotatef(angle, 0.0, 0.0, 1.0)  
        glCallList(arbol.gl_list)
        glPopMatrix()



        glPushMatrix()
        glRotatef(180, 1, 0, 0)
        glCallList(obj.gl_list)
        glPopMatrix()





  

        


        for i in range(len(posiciones)):
            glPushMatrix()
            glTranslatef(posiciones[i][0],posiciones[i][1],-40)
            glRotatef(angle, 0.0, 1.0, 0.0) 
            glCallList(estrella.gl_list)
            glPopMatrix()



        pygame.display.flip()
        pygame.time.wait(10)
    

  
        angle += speed


main()

import pygame
import random

#FUNCIONES

# Dibujamos las casillas
def boxGenerator(box_number,box_x, box_y):

    img = pygame.image.load("NoDescubierta.png")
    screen.blit(img,(box_x,box_y))

    valueGenerator()
    box_number = box_number-1
    return box_number
    
# Desplegar casillas
def fieldGenerator(box_number,box_x, box_y, box_width, box_height,box_pixels):
    for each in range(box_number):
        if box_number > 0:
            pintar=True
        if pintar:
            box_number = boxGenerator(box_number,box_x, box_y, box_width, box_height)
            pintar=False
            
        if box_x < width-box_pixels:
            box_x= box_x+ box_pixels
        else:
            box_y= box_y+ box_pixels
            box_x = 0

# Generar valor casilla
def valueGenerator():
    if(num_minas<=0):
        box_value =0
        return box_value 
    else:
        box_value=random.randint(0,1)
        print (box_value)
        return box_value

#PARÁMETROS

# Información pantalla
width = 640
height = 640
FPS_RELOJ = pygame.time.Clock()

# Selector de numero de casillas
box_number = 64

# Numero de pixeles por lado de la casilla
box_pixels = 80 

# Información varia de las casillas
box_value = []   # 0 nada | 1 bomba | 2 uno | 3 dos | 4 tres | 5 cuatro

num_minas = 10

box_x = 0
box_y = 0

box_width = box_pixels
box_height = box_pixels

#EJECUCIÓN

# Inicializa el entorno de pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Buscaminas')

running = True

# Generación de casillas
fieldGenerator(box_number,box_x, box_y, box_width, box_height, box_pixels)

# While
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            
    keyPressed = pygame.key.get_pressed()

    #Detector de clicks y posicion
    if event.type == pygame.MOUSEBUTTONDOWN:
        izquierdo, medio, derecho = pygame.mouse.get_pressed()
        if (izquierdo):
            print("Click Izquierdo")
        elif(medio):
            print("Click Medio")
        elif(derecho):
            print("Click Derecho")
        pos_raton = pygame.mouse.get_pos()
        print(pos_raton)
    
    # Salir con la tecla Q
    if keyPressed[pygame.K_q]: 
        print("Saliendo")
        running = False
    
        
    # Actualizamos la pantalla
    pygame.display.update()
    FPS_RELOJ.tick(60)
    
    
    
pygame.quit()
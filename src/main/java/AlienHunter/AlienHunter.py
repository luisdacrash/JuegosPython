import pygame
import array
import random
import time

#-----METODOS-----
def crearMira(spritesDelJuego):
    
    # Creamos un Sprite para el mira
    imagen_mira = pygame.sprite.Sprite()
    
    # Cargamos el fichero de imágenes
    imagen_mira = pygame.image.load("mira.png").convert()

    mira = imagen_mira.get_rect()

    # Añadimos el mira a los sprites del juego
    spritesDelJuego.add(mira)
    
    return mira

def update(mira): 
    # Desplazar izquierda/derecha
    mira.rect.x += pos_raton[0]

    # Desplazar arriba/abajo
    mira.rect.y += pos_raton[1]

#-----ATRIBUTOS-----
# Información pantalla
width = 1000
height = 1000
FPS_RELOJ = pygame.time.Clock()

spritesDelJuego = pygame.sprite.Group()

#-----BUCLE-----
# Inicializa el entorno de pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Buscaminas')

dimensiones = [width, height] 
pantalla = pygame.display.set_mode(dimensiones) 

# Creamos al mira
mira = crearMira(spritesDelJuego)

running = True

while running:

    pos_raton = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            
    keyPressed = pygame.key.get_pressed()

    #Detector de clicks y posicion raton
    if event.type == pygame.MOUSEBUTTONDOWN:
        izquierdo, medio, derecho = pygame.mouse.get_pressed()
        if (izquierdo):
            print(pos_raton)
        elif(medio):
            print("Click Medio")
        elif(derecho):
            print(pos_raton)
    
    # Actualizamos la mira. 
    update(mira)

    # Actualizamos la pantalla
    pygame.display.update()
    FPS_RELOJ.tick(60)

pygame.quit()
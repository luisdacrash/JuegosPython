import pygame, sys
from pygame.locals import *
from random import randint
import time

pygame.init()

#FUNCIONES----------------------------------------
def Pregunta1(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5):
    pregunta="¿De que se compone el anillo de Saturno?"
    respuesta1="Gases"
    respuesta2="Piedras"
    respuesta3="Vapor de Agua"
    respuesta4="Otros planetas"
    respuesta5="Cometas"
    respuesta1_Corr=False
    respuesta2_Corr=True
    respuesta3_Corr=False
    respuesta4_Corr=False
    respuesta5_Corr=False
    return pregunta, respuesta1,respuesta1_Corr, respuesta2,respuesta2_Corr, respuesta3,respuesta3_Corr, respuesta4,respuesta4_Corr, respuesta5,respuesta5_Corr

def Pregunta2(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5):
    pregunta="¿Que porcentaje de la Tierra está cubierta de agua?"
    respuesta1="25%"
    respuesta2="50%"
    respuesta3="75%"
    respuesta4="70%"
    respuesta5="40%"
    respuesta1_Corr=False
    respuesta2_Corr=False
    respuesta3_Corr=False
    respuesta4_Corr=True
    respuesta5_Corr=False
    return pregunta, respuesta1,respuesta1_Corr, respuesta2,respuesta2_Corr, respuesta3,respuesta3_Corr, respuesta4,respuesta4_Corr, respuesta5,respuesta5_Corr

def Pregunta3(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5):
    pregunta="¿Cuanto tiempo tarda la Tierra en dar una vuelta al sol?"
    respuesta1=""
    respuesta2=""
    respuesta3=""
    respuesta4=""
    respuesta5=""
    respuesta1_Corr=False
    respuesta2_Corr=False
    respuesta3_Corr=False
    respuesta4_Corr=False
    respuesta5_Corr=False
    return pregunta, respuesta1,respuesta1_Corr, respuesta2,respuesta2_Corr, respuesta3,respuesta3_Corr, respuesta4,respuesta4_Corr, respuesta5,respuesta5_Corr

def Pregunta4(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5):
    pregunta="a"
    respuesta1=""
    respuesta2=""
    respuesta3=""
    respuesta4=""
    respuesta5=""
    respuesta1_Corr=False
    respuesta2_Corr=False
    respuesta3_Corr=False
    respuesta4_Corr=False
    respuesta5_Corr=False
    return pregunta, respuesta1,respuesta1_Corr, respuesta2,respuesta2_Corr, respuesta3,respuesta3_Corr, respuesta4,respuesta4_Corr, respuesta5,respuesta5_Corr

def Pregunta5(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5):
    pregunta="a"
    respuesta1=""
    respuesta2=""
    respuesta3=""
    respuesta4=""
    respuesta5=""
    respuesta1_Corr=False
    respuesta2_Corr=False
    respuesta3_Corr=False
    respuesta4_Corr=False
    respuesta5_Corr=False
    return pregunta, respuesta1,respuesta1_Corr, respuesta2,respuesta2_Corr, respuesta3,respuesta3_Corr, respuesta4,respuesta4_Corr, respuesta5,respuesta5_Corr


#PARAMETROS--------------------------------------

#Ventana
width = 1000
heigth = 1000
ventana = pygame.display.set_mode((width,heigth))
pygame.display.set_caption("Alien Hunter")

#Texto
fuente = pygame.font.Font(None, 50)
fuenteRes = pygame.font.Font(None, 40)
fuentePreg = pygame.font.Font(None, 70)


#Mira
mira = pygame.image.load("mira.png")
mira_x, mira_y = 0,0
mira_col = pygame.Rect(mira_x,mira_y,10,10)

#Fondo
selva = pygame.image.load("selva.png")

#Alien1
alien1 = pygame.image.load("alien_azul.png")
alien1_x, alien1_y = randint(0,900),randint(250,900)
vel_alien1 = 4.5
alien1_col = pygame.Rect(alien1_x,alien1_y,47,45)

#Alien2
alien2 = pygame.image.load("alien_cian.png")
alien2_x, alien2_y = randint(-30,870),randint(250,870)
vel_alien2 = 3.5
alien2_col = pygame.Rect(alien2_x,alien2_y,30,90)

#Alien3
alien3 = pygame.image.load("alien_morado.png")
alien3_x, alien3_y = randint(-40,800),randint(250,800)
vel_alien3 = 2.5
vida_morado = 2
alien3_col = pygame.Rect(alien3_x,alien3_y,50,120)

#Alien4
alien4 = pygame.image.load("alien_rojo.png")
alien4_x, alien4_y = randint(-30,720),randint(250,720)
vel_alien4 = 1.5
vida_rojo=3
alien4_col = pygame.Rect(alien4_x,alien4_y,130,190)

#Alien5
alien5 = pygame.image.load("alien_verde.png")
alien5_x, alien5_y = randint(0,900),randint(250,900)
vel_alien5 = 5.5
alien5_col = pygame.Rect(alien5_x,alien5_y,38,38)

#Varios
puntuacion = 0
negro = pygame.Color(0,0,0)
if randint(1,2)==1:
    mov_alien1 = True
else: 
    mov_alien1 = False
if randint(1,2)==1:
    mov_alien2 = True
else: 
    mov_alien2 = False
if randint(1,2)==1:
    mov_alien3 = True
else: 
    mov_alien3 = False
if randint(1,2)==1:
    mov_alien4 = True
else: 
    mov_alien4 = False
if randint(1,2)==1:
    mov_alien5 = True
else: 
    mov_alien5 = False

#Variables Texto
pregunta="p"
respuesta1="r"
respuesta2="r"
respuesta3="r"
respuesta4="r"
respuesta5="r"

#Respuesta_Correcta
respuesta1_Corr=False
respuesta2_Corr=False
respuesta3_Corr=False
respuesta4_Corr=False
respuesta5_Corr=False

#Spawn Enemigos

alien1_alive = True
alien2_alive = True
alien3_alive = True
alien4_alive = True
alien5_alive = True

#Pregunta puesta
pregunta_puesta = False

#WHILE_PRINCIPAL--------------------------------
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            
    keyPressed = pygame.key.get_pressed()

    #Fondo
    ventana.blit(selva,(0,0))

    #Determinación pregunta
    if(pregunta_puesta==False):
        random= randint(1,5)
        if(random==1):
            pregunta,respuesta1,respuesta1_Corr,respuesta2,respuesta2_Corr,respuesta3,respuesta3_Corr,respuesta4,respuesta4_Corr,respuesta5,respuesta5_Corr=Pregunta1(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5)
            pregunta_puesta=True
        elif(random==2):
            pregunta,respuesta1,respuesta1_Corr,respuesta2,respuesta2_Corr,respuesta3,respuesta3_Corr,respuesta4,respuesta4_Corr,respuesta5,respuesta5_Corr=Pregunta2(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5)
            pregunta_puesta=True
        elif(random==3):
            pregunta,respuesta1,respuesta1_Corr,respuesta2,respuesta2_Corr,respuesta3,respuesta3_Corr,respuesta4,respuesta4_Corr,respuesta5,respuesta5_Corr=Pregunta3(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5)
            pregunta_puesta=True
        elif(random==4):
            pregunta,respuesta1,respuesta1_Corr,respuesta2,respuesta2_Corr,respuesta3,respuesta3_Corr,respuesta4,respuesta4_Corr,respuesta5,respuesta5_Corr=Pregunta4(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5)
            pregunta_puesta=True
        elif(random==5):
            pregunta,respuesta1,respuesta1_Corr,respuesta2,respuesta2_Corr,respuesta3,respuesta3_Corr,respuesta4,respuesta4_Corr,respuesta5,respuesta5_Corr=Pregunta5(pregunta,respuesta1,respuesta2,respuesta3,respuesta4,respuesta5)
            pregunta_puesta=True

    #Tiempo
    Tiempo = pygame.time.get_ticks()//1000
    contador = fuente.render("Tiempo: "+str(Tiempo),0,(255,255,255),(123,123,123))
    ventana.blit(contador,(810,0))

    #Texto
    texto = fuente.render("Puntuación: "+str(puntuacion),0,(255,255,255),(123,123,123))
    ventana.blit(texto,(5,5))

    texto = fuente.render("Pregunta: "+pregunta,0,(255,255,255),(123,123,123))
    ventana.blit(texto,(300,125))
    
    #Alien1
    if alien1_alive ==True:
        pygame.draw.rect(ventana,(0,0,255),alien1_col)
        alien1_col.left, alien1_col.top = alien1_x+25, alien1_y+25
        ventana.blit(alien1,(alien1_x,alien1_y))
        res1 = fuenteRes.render(respuesta1,0,(0,0,0),(255,255,255))
        ventana.blit(res1,(alien1_x-30,alien1_y-30))
    #Alien2
    if alien2_alive ==True:
        pygame.draw.rect(ventana,(0,255,225),alien2_col)
        alien2_col.left, alien2_col.top = alien2_x+67, alien2_y+50
        ventana.blit(alien2,(alien2_x,alien2_y))
        res2 = fuenteRes.render(respuesta2,0,(0,0,0),(255,255,255))
        ventana.blit(res2,(alien2_x-3,alien2_y-30))
    #Alien3
    if alien3_alive ==True:
        pygame.draw.rect(ventana,(128,0,128),alien3_col)
        alien3_col.left, alien3_col.top = alien3_x+105, alien3_y+40
        ventana.blit(alien3,(alien3_x,alien3_y))
        res3 = fuenteRes.render(respuesta3,0,(0,0,0),(255,255,255))
        ventana.blit(res3,(alien3_x+44,alien3_y-30))
    #Alien4
    if alien4_alive ==True:
        pygame.draw.rect(ventana,(255,255,255),alien4_col)
        alien4_col.left, alien4_col.top = alien4_x+80, alien4_y+60
        ventana.blit(alien4,(alien4_x,alien4_y))
        res4 = fuenteRes.render(respuesta4,0,(0,0,0),(255,255,255))
        ventana.blit(res4,(alien4_x+55,alien4_y-25))
    #Alien5
    if alien5_alive ==True:
        pygame.draw.rect(ventana,(0,200,0),alien5_col)
        alien5_col.left, alien5_col.top = alien5_x+32, alien5_y+42
        ventana.blit(alien5,(alien5_x,alien5_y))
        res5 = fuenteRes.render(respuesta5,0,(0,0,0),(255,255,255))
        ventana.blit(res5,(alien5_x-27,alien5_y-30))

    #Mira
    pygame.draw.rect(ventana,(255,0,0),mira_col)
    mira_col.left, mira_col.top = mira_x+96, mira_y+100
    ventana.blit(mira,(mira_x,mira_y))
    mira_x, mira_y = pygame.mouse.get_pos()
    mira_x-=101
    mira_y-=105
    
    #Movimiento Alien_Azul
    if mov_alien1 == True:
        if alien1_x<=900:
            alien1_x +=vel_alien1
        else:
            mov_alien1 = False
    else:
        if alien1_x>=0:
            alien1_x -=vel_alien1
        else:
            mov_alien1 = True
    
    #Movimiento Alien_Cian
    
    if mov_alien2 == True:
        if alien2_x<=870:
            alien2_x +=vel_alien2
        else:
            mov_alien2 = False
    else:
        if alien2_x>=-30:
            alien2_x -=vel_alien2
        else:
            mov_alien2 = True
    
    #Movimiento Alien_Morado
    if mov_alien3 == True:
        if alien3_x<=800:
            alien3_x +=vel_alien3
        else:
            mov_alien3 = False
    else:
        if alien3_x>=-40:
            alien3_x -=vel_alien3
        else:
            mov_alien3 = True
    
    #Movimiento Alien_Rojo
    if mov_alien4 == True:
        if alien4_x<=720:
            alien4_x +=vel_alien4
        else:
            mov_alien4 = False
    else:
        if alien4_x>=-30:
            alien4_x -=vel_alien4
        else:
            mov_alien4 = True
    
    #Movimiento Alien_Verde
    if mov_alien5 == True:
        if alien5_x>=0:
            alien5_x -=vel_alien5
        else:
            mov_alien5 = False
    else:
        if alien5_x<=900:
            alien5_x +=vel_alien5
        else:
            mov_alien5 = True
    
    #Detector de clicks y posicion raton
    if event.type == pygame.MOUSEBUTTONDOWN:
        izquierdo, medio, derecho = pygame.mouse.get_pressed()
        if (izquierdo):
            #Detectar Colisión
            if alien1_alive==True and alien1_col.colliderect(mira_col):
                vel_alien1 = 0
                puntuacion +=10
                alien1_alive = False
                if(respuesta1_Corr):
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("CORRECTO!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)
                else:
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("ERROR!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)
                
            if alien2_alive==True and alien2_col.colliderect(mira_col):
                vel_alien2 = 0
                puntuacion +=10
                alien2_alive = False
                if(respuesta2_Corr):
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("CORRECTO!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)
                else:
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("ERROR!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)
                
            if alien3_alive==True and alien3_col.colliderect(mira_col):
                vel_alien3 = 0
                puntuacion +=10
                alien3_alive = False
                if(respuesta3_Corr):
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("CORRECTO!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)
                else:
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("ERROR!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)
                
            if alien4_alive==True and alien4_col.colliderect(mira_col):
                vel_alien4 = 0
                puntuacion +=10
                alien4_alive = False
                if(respuesta4_Corr):
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("CORRECTO!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)
                else:
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("ERROR!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)
                
            if alien5_alive==True and alien5_col.colliderect(mira_col):
                vel_alien5 = 0
                puntuacion +=10
                alien5_alive = False
                if(respuesta5_Corr):
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("CORRECTO!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)
                else:
                    ventana.blit(selva,(0,0))
                    texto = fuente.render("ERROR!!",0,(255,255,255),(123,123,123))
                    ventana.blit(texto,(300,125))
                    pygame.display.update()
                    time.sleep(0.75)

        elif(medio):
            print("Click Medio")
        elif(derecho):
            print("Click Derecho")
    pygame.display.update()
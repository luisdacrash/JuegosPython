import pygame
import random

#FUNCIONES
#Generación de las casillas
def genBox(box_x,box_y, box_value): 
    if(box_value>=10):
        img = pygame.image.load("NoDescubierta.png")
        screen.blit(img,(box_x,box_y))
    elif(box_value<10):
        if(box_value==2):
            img = pygame.image.load("Uno.png")
            screen.blit(img,(box_x,box_y))
            pygame.time.wait(100)

        if(box_value==1):
            img = pygame.image.load("Bombas.png")
            screen.blit(img,(box_x,box_y))
            pygame.time.wait(100)

        if(box_value==6):
            img = pygame.image.load("Bandera.png")
            screen.blit(img,(box_x,box_y))

        if(box_value==5):
            img = pygame.image.load("Cuatro.png")
            screen.blit(img,(box_x,box_y))

        if(box_value==0):
            img = pygame.image.load("Descubierta.png")
            screen.blit(img,(box_x,box_y))
            
        if(box_value==3):
            img = pygame.image.load("Dos.png")
            screen.blit(img,(box_x,box_y))

        if(box_value==4):
            img = pygame.image.load("Tres.png")
            screen.blit(img,(box_x,box_y))

def descBox(x,y, box_value,pos_valor): 
    soy_mina = False
    minas_cerca = 0
    print(pos_valor)
    if(pos_valor<=63):
        if(((box_value[pos_valor+6])-10)==1):
                minas_cerca+=1
        if(((box_value[pos_valor-7])-10)==1):
                minas_cerca+=1
        if(((box_value[pos_valor-8])-10)==1):
                minas_cerca+=1
        if(((box_value[pos_valor-1])-10)==1):
                minas_cerca+=1
        if(((box_value[pos_valor+1])-10)==1):
                minas_cerca+=1
        if(((box_value[pos_valor+6])-10)==1):
                minas_cerca+=1
        if(((box_value[pos_valor+7])-10)==1):
                minas_cerca+=1
        if(((box_value[pos_valor+8])-10)==1):
                minas_cerca+=1
        if(((box_value[pos_valor])-10)==1):
                soy_mina = True

    print("minas cerca ",minas_cerca,soy_mina)
    if(minas_cerca==1):
        box_value[pos_valor]=2
    if(minas_cerca==2):
        box_value[pos_valor]=3
    if(minas_cerca==3):
        box_value[pos_valor]=4
    if(minas_cerca==4):
        box_value[pos_valor]=5
    if(soy_mina):
        box_value[pos_valor]=1

    box_value= box_value[pos_valor]

    box_x=x*box_pixels
    box_y=y*box_pixels
    genBox(box_x, box_y, box_value)
    
    
def descubrirCasilla(pos_raton):
    x=int(pos_raton[0] / box_pixels)
    y=int(pos_raton[1] / box_pixels)
    print(x,y)
    pos_valor=((x*8)+y)
    if(box_value[pos_valor]>=0):
        box_value[pos_valor]-=10
    print(box_value[pos_valor])
    descBox(x,y,box_value,pos_valor)

def CasillaBandera(pos_raton):
    x=int(pos_raton[0] / box_pixels)
    y=int(pos_raton[1] / box_pixels)
    print(x,y)
    pos_valor=((x*8)+y)
    if(box_value[pos_valor]>=0):
        box_value[pos_valor]-=10
    box_value[pos_valor]=6
    print(box_value[pos_valor])
    descBox(x,y,box_value,pos_valor)

def valueGenerator(num_minas):
    valor = 0
    if(num_minas<=0):
        valor=0
        return valor+10
    else:
        a=random.randint(0,12)
        if(a<=1):
            valor=1
        print (valor)
        return valor+10

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
box_value = []   # >7 no descubierta | 1 bomba | 2 uno | 3 dos | 4 tres | 5 cuatro | 6 bandera | 7 descubierta

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
for i in range (box_number):
    box_value.append(valueGenerator(num_minas))
    if(box_value[i]==11):
            num_minas=num_minas-1
    genBox(box_x,box_y,box_value[i])

    if box_x < width-box_pixels:
            box_x= box_x+ box_pixels
    else:
            box_y= box_y+ box_pixels
            box_x = 0

# While
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            
    keyPressed = pygame.key.get_pressed()

    #Detector de clicks y posicion
    if event.type == pygame.MOUSEBUTTONDOWN:
        izquierdo, medio, derecho = pygame.mouse.get_pressed()
        pos_raton = pygame.mouse.get_pos()
        pygame.time.wait(250)
        if (izquierdo):
            descubrirCasilla(pos_raton)
        elif(medio):
            print("Click Medio")
        elif(derecho):
            CasillaBandera(pos_raton)
        print(pos_raton)
    
    # Salir con la tecla Q
    if keyPressed[pygame.K_q]: 
        print("Saliendo")
        running = False
    
    # Calcular tiempo transcurrido
    tiempo_transcurrido = (pygame.time.get_ticks()) / 1000

    # Tiempo en texto
    texto_tiempo = "Tiempo restante: " + str(60 - int(tiempo_transcurrido)) + " segundos"
    pygame.display.set_caption('Buscaminas - ' + texto_tiempo)
    if (60 - int(tiempo_transcurrido))==0: 
        print("Se acabó el tiempo")
        running = False
        
    # Actualizamos la pantalla
    pygame.display.update()
    FPS_RELOJ.tick(60)
    
    
    
pygame.quit()
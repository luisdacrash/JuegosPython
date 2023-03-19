import pygame
import random
import array
import asyncio

async def main():

    #FUNCIONES
    #Generación de las casillas
    def gameout():
        pygame.quit()
    def gameOver():
        box_x=0
        box_y=0
        img2 = pygame.image.load("gameover.png")
        screen.blit(img2,(box_x,box_y))
        pygame.display.flip()
        pygame.time.wait(2000)
        gameout()
        
    def genBox(box_x,box_y, box_value):     
        print(box_value)
        if(box_value>=10):
            img = pygame.image.load("NoDescubierta.png")
            screen.blit(img,(box_x,box_y))
        if(box_value<10):
            if(box_value==2):
                img = pygame.image.load("Uno.png")
                screen.blit(img,(box_x,box_y))
                pygame.time.wait(100)

            if(box_value==1):
                img = pygame.image.load("Bombas.png")
                screen.blit(img,(box_x,box_y))
                pygame.display.flip()
                pygame.time.wait(1000)
                gameOver()

            if(box_value==16):
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

    def descBox(x,y, box_value): 
        soy_mina = False
        minas_cerca = 0
        print("aaaaaaaaaa" , box_value[y][x])
        if(y<7 and x<7):
            if(((box_value[y+1][x-1]))==11):
                        minas_cerca+=1

            if(((box_value[y][x-1]))==11):
                        minas_cerca+=1

            if(((box_value[y-1][x-1]))==11):
                        minas_cerca+=1

            if(((box_value[y+1][x]))==11):
                        minas_cerca+=1
                        
            if(((box_value[y-1][x]))==11):
                        minas_cerca+=1

            if(((box_value[y-1][x+1]))==11):
                        minas_cerca+=1

            if(((box_value[y][x+1]))==11):
                        minas_cerca+=1

            if(((box_value[y+1][x+1]))==11):
                        minas_cerca+=1

            if(((box_value[y][x]))==11):
                        soy_mina = True   
        if(y<7 and x==7):
            if(((box_value[y+1][x-1]))==11):
                        minas_cerca+=1

            if(((box_value[y][x-1]))==11):
                        minas_cerca+=1

            if(((box_value[y-1][x-1]))==11):
                        minas_cerca+=1

            if(((box_value[y+1][x]))==11):
                        minas_cerca+=1
                        
            if(((box_value[y-1][x]))==11):
                        minas_cerca+=1

            if(((box_value[y][x]))==11):
                        soy_mina = True   
        if(y==7 and x<7):
            if(((box_value[y][x-1]))==11):
                        minas_cerca+=1

            if(((box_value[y-1][x-1]))==11):
                        minas_cerca+=1
                        
            if(((box_value[y-1][x]))==11):
                        minas_cerca+=1

            if(((box_value[y-1][x+1]))==11):
                        minas_cerca+=1

            if(((box_value[y][x+1]))==11):
                        minas_cerca+=1

            if(((box_value[y][x]))==11):
                        soy_mina = True  
        if(y==7 and x==7):
            if(((box_value[y][x-1]))==11):
                        minas_cerca+=1

            if(((box_value[y-1][x-1]))==11):
                        minas_cerca+=1
                        
            if(((box_value[y-1][x]))==11):
                        minas_cerca+=1

            if(((box_value[y][x]))==11):
                        soy_mina = True  
            
        
        box_x=x*box_pixels
        box_y=y*box_pixels

        print("minas cerca ",minas_cerca,soy_mina)
        if(minas_cerca==0):
            box_value=0
        if(minas_cerca==1):
            box_value=2
        if(minas_cerca==2):
            box_value=3
        if(minas_cerca==3):
            box_value=4
        if(minas_cerca==4):
            box_value=5
        if(soy_mina):
            box_value=1
        genBox(box_x, box_y, box_value)
        
        
    def descubrirCasilla(pos_raton):
        x=int(pos_raton[0] / box_pixels)
        y=int(pos_raton[1] / box_pixels)
        print(x,y)
        print(box_gen[y][x])
        descBox(x,y,box_gen)

    def CasillaBandera(pos_raton):
        x=int(pos_raton[0] / box_pixels)
        y=int(pos_raton[1] / box_pixels)
        print(x,y)
        print(box_gen[y][x])
        descBox(x,y,box_gen)

    def valueGenerator(num_minas):
        valor = 0
        if(num_minas<=0):
            valor=10
            return valor
        else:
            a=random.randint(0,10)
            if(a<=1):
                valor=11
            elif(a>1):
                valor=10
            print (valor)
            num_minas=num_minas-1
            return valor

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
    num_minas = 10

    box_gen_x = 9
    box_gen_y = 9 # >7 no descubierta | 1 bomba | 2 uno | 3 dos | 4 tres | 5 cuatro | 6 bandera | 7 descubierta
    box_gen = [[valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas)],[valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas)],[valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas)],[valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas)],[valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas)],[valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas)],[valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas)],[valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas),valueGenerator(num_minas)]]



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
    for columns in box_gen:
        for rows in columns:
            genBox(box_x,box_y,rows)

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
        await asyncio.sleep(0)
asyncio.run(main())
        
        
        
    
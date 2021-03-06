#Autor: José Luis Macías Vázquez. Grupo 03
#Misión 5.

import pygame
import random
import math


ANCHO = 800

ALTO = 800

NEGRO = (0,0,0)

BLANCO = (255,255,255)






def asignarColores():

    VERDE = random.randint(0, 255)

    ROJO = random.randint(0, 255)

    AZUL = random.randint(0, 255)

    return (VERDE, ROJO, AZUL)

def trazarLineas(ventana):

    for coorU in range(0, ALTO//2, 10):

        equis1 = 10 + coorU

        col = asignarColores()

        pygame.draw.line(ventana,col ,(ANCHO//2, coorU), (ANCHO//2 + equis1, ALTO//2))

    for coorD in range(0, ALTO//2, 10):

        equis2 = 10 + coorD

        col = asignarColores()

        pygame.draw.line(ventana, col,(ANCHO//2, coorD), (ANCHO//2 - equis2, ALTO//2))

    for coorT in range(0, ALTO//2, 10):

        equis3 = 10 +coorT + 10

        col = asignarColores()

        pygame.draw.line(ventana,col,(ANCHO//2, ALTO- coorT), (ANCHO//2 - equis3, ALTO//2))

    for coorC in range(0,ALTO//2,10):

        equis4 = 10 + coorC + 10

        col = asignarColores()

        pygame.draw.line(ventana,col,(ANCHO//2,ALTO- coorC), (ANCHO//2 + equis4, ALTO//2))

def dibujarEstrella():

    # Inicializa el motor de pygame
    pygame.init()

    # Crea una ventana de ANCHO x ALTO

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará

    reloj = pygame.time.Clock()  # Para limitar los fps

    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente

        # Procesa los eventos que recibe

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir

                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        trazarLineas(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)

        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def dibujarCircCuad(ventana):

    for medCirc in range(10 , ALTO //2, 10):

        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2) , medCirc, 1)

        pygame.draw.rect(ventana, NEGRO, (ANCHO//2- medCirc, ALTO//2-medCirc, medCirc*2, medCirc*2), 1)



def dibujarCirculosCuadrados():

        # Inicializa el motor de pygame
        pygame.init()

        # Crea una ventana de ANCHO x ALTO

        ventana = pygame.display.set_mode((ANCHO, ALTO))# Crea la ventana donde dibujará

        reloj = pygame.time.Clock()# Para limitar los fps

        termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

        while not termina: # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente

            # Procesa los eventos que recibe
            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:# El usuario hizo click en el botón de salir

                    termina = True# Queremos terminar el ciclo

            # Borrar pantalla
            ventana.fill(BLANCO)

            # Dibujar, aquí haces todos los trazos que requieras
            # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
            # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
            dibujarCircCuad(ventana)

            pygame.display.flip()# Actualiza trazos (Si no llamas a esta función, no se dibuja)

            reloj.tick(40)# 40 fps

        # Después del ciclo principal
        pygame.quit()# termina pygame


        dibujarCircCuad(ventana)

def trazarCirculos(ventana):

    for circ in range(30,361,30):

        girCirc = math.radians(circ)

        ejeX = math.cos(girCirc)*150

        ejeY = math.sin(girCirc)*150

        pygame.draw.circle(ventana, NEGRO, (int(ejeX + ANCHO//2), int(ALTO//2-ejeY)), 150, 1)

def dibujarCirculos():

    # Inicializa el motor de pygame
    pygame.init()

    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará

    reloj = pygame.time.Clock()  # Para limitar los fps

    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente

        # Procesa los eventos que recibe
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir

                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        trazarCirculos(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)

        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def aproximarPi(apro):

    suma = 0

    for n in range(1, apro + 1):

        frac = 1 / n ** 2

        suma +=  frac


    aproP = (suma * 6) ** 0.5

    print(aproP)

def calcularNumeros():

    cont = 0

    for n in range(1000, 10000, 1):

        if n%37 == 0:

            cont += 1

        else:

            cont = cont

    print(cont)

def imprimirPiramide():

    a = 0

    b = 0

    for ch in range(0, 9, 1):

        base = 10 ** ch

        a = base + a

        b = b + a

        d = b * 8 + (ch + 1)

        print(b, "* 8 +", ch + 1, "=", d)

    print()

    cam = 0

    for e in range(0, 9, 1):

        base2 = 10 ** e

        cam += base2

        pir = cam * cam

        print(cam, "*", cam, "=", pir)



def main():

    print("""Misión 5. Seleccione qué quiere hacer.
    1. Dibujar cuadros y círculos 
    2. Dibujar parábolas 
    3. Dibujar círculos 
    4. Aproximar PI
    5. Contar divisibles entre 37 
    6. Imprimir pirámides de números 
    0. Salir """)

    selec = int(input("Digite el número de la opción: "))

    while selec != 0:

        if selec == 1:

            dibujarCirculosCuadrados()

        elif selec == 2:

            dibujarEstrella()

        elif selec == 3:

            dibujarCirculos()

        elif selec == 4:

            apro = int(input("Digíte el numero que aproximará a PI: "))

            aproximarPi(apro)


        elif selec == 5:

                calcularNumeros()

        elif selec == 6:

                imprimirPiramide()

        selec = int(input("¿Qué desea hacer?: "))

main()
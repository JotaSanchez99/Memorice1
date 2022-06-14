from sunau import AUDIO_UNKNOWN_SIZE
from turtle import exitonclick, st
import pygame
import os.path
from pygame.locals import *
from pygame import *
import threading
import math
import random

#VERIFICAR SI EXISTE EL MODULO DE IMAGEN, SINO, TIRAR ERROR
if not pygame.image.get_extended():
    raise SystemExit("Perdon, algo salio mal")

#VARIABLES GLOBALES
SCREENRECT = Rect(0, 0, 640, 480)
MARGEN_TARJETA = 50
PADDING_TARJETA = 4

#CARPETA RAIZ, DONDE ESTAN TODOS LOS ARCHIVOS DEL JUEGO Y ESTA CLASE
main_dir = os.path.split(os.path.abspath(__file__))[0]




#FUNCIONES

def cargar_imagenes(*archivos):
    imgs = []
    for archivo in archivos:
        imgs.append(cargar_imagen(archivo))
    return imgs

ANCHO = 1200
ALTURA = 750
TARJETA_ACTUAL = None
TARJETA_ACTUAL = None


#CARGAR IMAGEN
def cargar_imagen(nombrearchivo, transparent=False):
    try:
        imagen = pygame.image.load(nombrearchivo)
    except pygame.error:
        raise SystemExit
    imagen = imagen.convert()
    if transparent:
        color = imagen.get_at((0, 0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen

#Comprobar
def comprobar(tarjeta):
    global TARJETA_ACTUAL

    if TARJETA_ACTUAL == None:
        tarjeta.voltear()
        TARJETA_ACTUAL = tarjeta
    else:
        tarjeta.voltear()
        if TARJETA_ACTUAL.id == tarjeta.id:
            print("Coinciden!!!")
            TARJETA_ACTUAL.image.set_alpha(80)
            tarjeta.image.set_alpha(80)
            TARJETA_ACTUAL = None
        else:
            print("No coinciden.")

            def func():
                global TARJETA_ACTUAL
                tarjeta.pressed = False
                tarjeta.voltear()
                TARJETA_ACTUAL.voltear()
                TARJETA_ACTUAL.pressed = False
                TARJETA_ACTUAL = None

            set_timeout(func, 1.0)  # This is 0.1s = 100ms


#TEMPORIZADOR
def set_timeout(func, sec):
    t = None
    def func_wrapper():
        func()
        t.cancel()
    t = threading.Timer(sec, func_wrapper)
    t.start()

'''
Tiempo
#def tiempo:
Tiempo = pygame.ti
 #   pygame.
 Tiempo= pygame.time.get_ticks/1000
if aux==Tiempo:
    aux+=1
    print Tiempo
'''



#CLASE TARJETA
class Tarjeta(pygame.sprite.Sprite):
    global PADDING_TARJETA

    def __init__(self, data):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(cargar_imagen("tarjeta.jpg"))
        self.images.append(cargar_imagen(data[0]))
        self.rect = self.images[0].get_rect()
        self.rect.centerx = PADDING_TARJETA
        self.rect.centery = 100
        self.image = self.images[0]
        self.volteada = False
        self.id = data[1]
        self.pressed = False

    def voltear(self):
        if not self.volteada:
            self.image = self.images[1]
            self.volteada = True
        else:
            self.image = self.images[0]
            self.volteada = False

    def mouseEvent(self, type):
            if type == "click":
                if not self.pressed:
                    comprobar(self)
                    self.pressed = True


#CLASE PRINCIPAL
def main():
    screen = pygame.display.set_mode((ANCHO, ALTURA))
    pygame.display.set_caption("Numero 13")
    
    Fuente = pygame.font.SysFont("Arial",31)
    

    background = cargar_imagen('fondo.jpg')
    background = pygame.transform.scale(background, (ANCHO, ALTURA))
    displaylist = []
    global PADDING_TARJETA
    global MARGEN_TARJETA

    tarjetas = [("tarjeta1.jpg", "Debian"), ("tarjeta1.jpg", "Debian"),
                ("tarjeta2.jpg", "Archi"), ("tarjeta2.jpg", "Archi"),
                ("tarjeta3.jpg", "Mint"),("tarjeta3.jpg", "Mint"),
                ("tarjeta4.jpg", "Ubuntu"), ("tarjeta4.jpg", "Ubuntu"),
                ("tarjeta5.jpg", "Aple"), ("tarjeta5.jpg", "Aple"),
                ("tarjeta6.jpg", "kali"), ("tarjeta6.jpg", "kali"),
                ("tarjeta7.jpg", "Parrot"), ("tarjeta7.jpg", "Parrot"),
                ("tarjeta8.jpg", "win"), ("tarjeta8.jpg", "win"),
                ("tarjeta9.jpg", "Redhat"), ("tarjeta9.jpg", "Redhat")]

    random.shuffle(tarjetas)

    for i in range(0, len(tarjetas)):
        tarjeta = Tarjeta(tarjetas[i])
        tarjeta.rect.centerx = MARGEN_TARJETA + ((i % 6) * (tarjeta.rect.width+PADDING_TARJETA))
        tarjeta.rect.centery = MARGEN_TARJETA + (math.floor(i / 6) * (tarjeta.rect.height + PADDING_TARJETA))
        displaylist.append(tarjeta)
        
    aux=1
    while True:
        
        Tiempo= pygame.time.get_ticks()/1000
        if aux == Tiempo:
            aux+=1
            print(Tiempo)
        #print(Tiempo)
        
        for evento in pygame.event.get():
            #print(event)
              
            if evento.type == pygame.QUIT:
                sys.exit()
                
            if evento.type == pygame.MOUSEBUTTONUP:
                if(evento.button == 1):
                    x, y = evento.pos

                    for i in range(0, len(displaylist)):
                        child = displaylist[i]
                        if child.rect.collidepoint(x, y):
                            child.mouseEvent("click")

        screen.blit(background, (0,0))
        for i in range(0, len(displaylist)):
            screen.blit(displaylist[i].image, displaylist[i].rect)

        contador= Fuente.render("Tiempo; "+str(Tiempo),0,(100,100,100))
        
        screen.blit(contador,(950,600))
        
        pygame.display.flip()
        pygame.display.update()


    return 0

#INICIAR
if __name__ == '__main__':
    pygame.init()
    main()
import pygame.font
from PPlay.window import*
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *


def navePad(janela,nave,velnavex,tiro,veltiro,t):
    teclado = Window.get_keyboard()
    # pad da nave
    if (teclado.key_pressed("A")):
        if nave.x == 0:
            velnavex = 0

        else:
            nave.x = nave.x + velnavex * janela.delta_time() * (-1)

    if (teclado.key_pressed("D")):
        if nave.x == janela.width - nave.width:
            velx = 0

        else:
            nave.x = nave.x + velnavex * janela.delta_time()

    if t==False:
        tiro.x = nave.x
        tiro.y = nave.y

    if tiro.y <= 0:
        t = False

    if (teclado.key_pressed("K")):
        if t==False:
            t=True

    return t


import pygame.font
from PPlay.window import*
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *
import pads

def play():
    #criando janela
    janela2 = Window(1080,600)
    janela2.set_title("jogar")
    janela2.set_background_color((000, 000, 40))

    fundo = GameImage("back.jpg")

    teclado = Window.get_keyboard()

    # posição inicial da nave
    nave = Sprite('3.png')
    nave.x = janela2.width / 2 - nave.width / 2
    nave.y = janela2.height - nave.height
    velnavex=500

    #posição inicial do tiro
    tiro= Sprite('t.png')
    tiro.x=nave.x
    veltiro=-400
    tiro.y = nave.y


    t = False
    while True:
        #pad da nave

        t=pads.navePad(janela2,nave,velnavex,tiro,veltiro,t)

        if t==False:
            tiro.x=nave.x

        if t == True:
            tiro.y = tiro.y + veltiro * janela2.delta_time()

        fundo.draw()

        if t==True:
            tiro.draw()
        nave.draw()

        if (teclado.key_pressed("ESC")):
            janela2.close()

        janela2.update()



def dificuldade():
    nave = Sprite('3.png')

    janela = Window(1080, 600)
    janela.set_title("dificuldade")
    janela.set_background_color((000, 000, 20))
    teclado = Window.get_keyboard()
    mouse = Window.get_mouse()

    fonted2 = pygame.font.SysFont('arial', 65, False, False)
    titulo = "Dificuldade"

    fonted = pygame.font.SysFont('arial', 40, False, False)
    facil = "fácil"
    medio = "médio"
    dificil = "difícil"

    tela2 = pygame.display.set_mode((1080, 600))
    while True:
        n=False
        #facil
        if mouse.is_over_area((170, 300), (245, 350)):
            nave.x = 120
            nave.y = 300
            n = True
        #medio
        if mouse.is_over_area((462, 300), (570, 350)):
            nave.x = 415
            nave.y = 300
            n = True
        #dificil
        if mouse.is_over_area((800, 300), (900, 350)):
            nave.x = 750
            nave.y = 300
            n = True

        tela2.fill((000, 000, 20))
        #textos----------------------------------------------------------------------------------------
        textoFormatadoTitulo = fonted2.render(titulo, False, (250, 250, 250))
        textoFormatadoFacil = fonted.render(facil, False, (250, 250, 250))
        textoFormatadoMedio = fonted.render(medio, False, (250, 250, 250))
        textoFormatadoDificil = fonted.render(dificil, False, (250, 250, 250))

        tela2.blit(textoFormatadoTitulo, (350, 000))
        tela2.blit(textoFormatadoFacil, (170, 300))
        tela2.blit(textoFormatadoMedio, (465, 300))
        tela2.blit(textoFormatadoDificil, (800, 300))
        #------------------------------------------------------------------------------------------------
        if n==True:
            nave.draw()
        if (teclado.key_pressed("ESC")):
            janela.close()
        janela.update()



def ranking():
    janela = Window(1080, 600)
    janela.set_title("ranking")
    janela.set_background_color((000, 000, 20))
    teclado = Window.get_keyboard()
    while True:
        if (teclado.key_pressed("ESC")):
            janela.close()
        janela.update()







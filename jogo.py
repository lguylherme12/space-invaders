# jogar com a tecla A para mover nave para direita, D para mover para a esqueda e K para atirar

import pygame.font
from PPlay.window import*
from PPlay.sprite import *
from PPlay.collision import *
from PPlay.mouse import *
from PPlay.gameimage import *
import janelas


#back = GameImage("back.jpg")
janela = Window(1080,600)
janela.set_title("menu")
mouse = Window.get_mouse()
teclado = Window.get_keyboard()

fonte= pygame.font.SysFont('arial',40, False, False)
fonte2= pygame.font.SysFont('arial',65, False, False)

jogar= "jogar"
dificuldade= "dificuldade"
ranking= "ranking"
sair = "sair"
titulo= "Space Invader"

nave= Sprite('3.png')

tela = pygame.display.set_mode((1080,600))

while True:
    m=False

    #jogar
    if mouse.is_over_area((100, 200), (190, 250)):
        nave.x=40
        nave.y=200
        m=True
        if (mouse.is_button_pressed(1)):
            janelas.play()

    #dificuldade
    if mouse.is_over_area((100, 300), (280, 350)):
        nave.x=40
        nave.y=300
        m=True
        if (mouse.is_button_pressed(1)):
            janelas.dificuldade()

    #ranking
    if mouse.is_over_area((100, 400), (230, 450)):
        nave.x=40
        nave.y=400
        m=True
        if (mouse.is_button_pressed(1)):
            janelas.ranking()

    #sair
    if mouse.is_over_area((100, 500), (170, 550)):
        nave.x=40
        nave.y=500
        m=True
        if (mouse.is_button_pressed(1)):
            janela.close()

    tela.fill((000, 000, 20))

    #textos-----------------------------------------------------------------------------------------
    textoFormatadoTitulo = fonte2.render(titulo, False, (250, 250, 250))
    textoFormatadoJogar= fonte.render(jogar,False,(250,250,250))
    textoFormatadoDificuldade = fonte.render(dificuldade, False, (250, 250, 250))
    textoFormatadoRanking = fonte.render(ranking, False, (250, 250, 250))
    textoFormatadoSair = fonte.render(sair, False, (250, 250, 250))

    janela.set_background_color((000, 000, 20))

    tela.blit(textoFormatadoTitulo, (330, 000))
    tela.blit(textoFormatadoJogar,(100,200))
    tela.blit(textoFormatadoDificuldade, (100, 300))
    tela.blit(textoFormatadoRanking, (100, 400))
    tela.blit(textoFormatadoSair, (100, 500))
    #----------------------------------------------------------------------------------------------------
    if m==True:
        nave.draw()
    #back.draw()
    janela.update()


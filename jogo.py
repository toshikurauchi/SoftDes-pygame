import pygame
from pygame.locals import *

class Jogo:
    def __init__(self):
        self.rodando = True

def eventos(jogo):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo.rodando = False
    
def atualiza(jogo):
    pass

def desenha(jogo):
    pass
 
pygame.init()
rodando = True
largura = 648
altura = 400
tela = pygame.display.set_mode((largura, altura), pygame.HWSURFACE | pygame.DOUBLEBUF)
jogo = Jogo()

while(jogo.rodando):
    eventos(jogo)
    atualiza(jogo)
    desenha(jogo)

pygame.quit()
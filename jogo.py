import pygame
from pygame.locals import *


VERDE = (0, 255, 0)
PRETO = (0, 0, 0)

TAMANHO = 20
GRAVIDADE = 0.2
PULO = -5


class Jogo:
    def __init__(self):
        self.rodando = True
        self.largura = 648
        self.altura = 400
        self.tela = pygame.display.set_mode((self.largura, self.altura))  # Tamanho da janela

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/raposa.png')
        self.image = pygame.transform.scale(self.image, (40, 35))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vy = 0

    def update(self):
        self.vy += GRAVIDADE
        self.rect.y += self.vy

    def pula(self):
        self.vy = PULO

def eventos(jogo, jogador):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo.rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogador.pula()

def atualiza(jogo, jogador_group):
    jogador_group.update()

def desenha(jogo, jogador_group):
    jogo.tela.fill(PRETO)

    # Pinta os elementos do grupo de jogadores na tela auxiliar.
    jogador_group.draw(jogo.tela)

    # Troca de tela na janela principal.
    pygame.display.update()

pygame.init()
rodando = True
jogo = Jogo()
pygame.display.set_caption('FlappInsper')  # Nome na aba

jogador = Jogador(20, jogo.altura / 2)
jogador_group = pygame.sprite.Group()
jogador_group.add(jogador)

while(jogo.rodando):
    eventos(jogo, jogador)
    atualiza(jogo, jogador_group)
    desenha(jogo, jogador_group)

pygame.quit()

import pygame
from pygame.locals import *


VERDE = (0, 255, 0)
PRETO = (0, 0, 0)

TAMANHO = 20
GRAVIDADE = 0.2
PULO = -5
FUNDO_VX = 1
OBSTACULO_VX = 2


class Jogo:
    def __init__(self):
        self.rodando = True
        self.largura = 648
        self.altura = 400
        self.tela = pygame.display.set_mode((self.largura, self.altura))  # Tamanho da janela
        self.fundo = pygame.image.load("assets/fundo.png")
        largura_fundo = int(self.fundo.get_width() * self.altura / self.fundo.get_height())
        self.fundo = pygame.transform.scale(self.fundo, (largura_fundo, self.altura))
        self.fundo_x = 0
        self.game_over = False

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y, jogo):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/raposa.png')
        self.image = pygame.transform.scale(self.image, (40, 35))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vy = 0
        self.jogo = jogo

    def update(self):
        self.vy += GRAVIDADE
        self.rect.y += self.vy
        max_y = self.jogo.altura - self.rect.height
        if self.rect.y > max_y:
            self.rect.y = max_y
            self.vy = 0
        elif self.rect.y < 0:
            self.rect.y = 0
            self.vy = 0

    def pula(self):
        self.vy = PULO

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, centro_x, centro_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/obstaculo.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = centro_x - self.image.get_width() / 2
        self.rect.y = centro_y - self.image.get_height() / 2

    def update(self):
        self.rect.x -= OBSTACULO_VX
        if self.rect.x + self.image.get_width() < 0:
            print('Killing')
            self.kill()

def eventos(jogo, jogador):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo.rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogador.pula()

def atualiza(jogo, jogador, obstaculos_group):
    jogo.fundo_x -= FUNDO_VX
    fundo_x_direita = jogo.fundo_x + jogo.fundo.get_width()
    if fundo_x_direita < 0:
        jogo.fundo_x = fundo_x_direita
    jogador.update()
    obstaculos_group.update()
    colisoes = pygame.sprite.spritecollide(jogador, obstaculos_group, False, pygame.sprite.collide_mask)
    if len(colisoes) > 0:
        jogo.game_over = True

def desenha(jogo, jogador_group, obstaculos_group):
    jogo.tela.blit(jogo.fundo, (jogo.fundo_x, 0))
    jogo.tela.blit(jogo.fundo, (jogo.fundo_x + jogo.fundo.get_width(), 0))

    # Pinta os elementos do grupo de jogadores na tela auxiliar.
    jogador_group.draw(jogo.tela)
    # Pinta os elementos do grupo de obstáculos na tela auxiliar.
    obstaculos_group.draw(jogo.tela)

    # Troca de tela na janela principal.
    pygame.display.update()

def eventos_gameover(jogo):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo.rodando = False

pygame.init()
rodando = True
jogo = Jogo()
pygame.display.set_caption('FlappInsper')  # Nome na aba

jogador = Jogador(20, jogo.altura / 2, jogo)
jogador_group = pygame.sprite.Group()
jogador_group.add(jogador)

obstaculo = Obstaculo(jogo.largura, jogo.altura / 2)
obstaculos_group = pygame.sprite.Group()
obstaculos_group.add(obstaculo)

while jogo.rodando and not jogo.game_over:
    eventos(jogo, jogador)
    atualiza(jogo, jogador, obstaculos_group)
    desenha(jogo, jogador_group, obstaculos_group)

while jogo.rodando and jogo.game_over:
    eventos_gameover(jogo)

pygame.quit()

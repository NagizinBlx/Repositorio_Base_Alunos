import pygame
import random
import sys

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA = 500
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mini Subway Surfers")

# Relógio
clock = pygame.time.Clock()
FPS = 60

# Jogador
jogador_larg = 50
jogador_alt = 50
jogador_x = LARGURA // 2 - jogador_larg // 2
jogador_y = ALTURA - jogador_alt - 20
velocidade = 7

# Obstáculos e

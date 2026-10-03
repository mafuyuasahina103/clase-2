import pygame
import random
import sys
import os

pygame.init()

ancho, alto= 800, 500
panatalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("robot esquiva meteoritos")
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("arial",24)


cielo =(10,10,40)

blanco =(255,255,255)

rojo =(260,50,50)

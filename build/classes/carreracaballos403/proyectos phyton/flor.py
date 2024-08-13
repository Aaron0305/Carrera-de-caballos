# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:24:09 2023

@author: DELL
"""

import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Flor Detallada")

# Colores
amarillo = (255, 255, 0)
verde = (0, 255, 0)
rojo = (255, 0, 0)

def dibujar_flor(x, y):
    # Dibuja el tallo
    pygame.draw.line(ventana, verde, (x, y), (x, y - 100), 10)

    # Dibuja los pétalos
    for angulo in range(0, 360, 45):
        radianes = math.radians(angulo)
        x_petal = x + 50 * math.cos(radianes)
        y_petal = y - 50 * math.sin(radianes)
        pygame.draw.ellipse(ventana, amarillo, (x_petal - 20, y_petal - 20, 40, 40))

    # Dibuja el centro de la flor
    pygame.draw.circle(ventana, rojo, (x, y - 50), 10)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill((255, 255, 255))
    dibujar_flor(ancho // 2, alto // 2)
    pygame.display.flip()

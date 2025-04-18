import pygame
import random
import time
import tkinter as tk
from tkinter import messagebox
from ranking.ranking_manager import actualizar_ranking,mostrar_ranking


def jugar(nombre):
    pygame.init()
    pantalla = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("🎯 Click the Target")
    fuente = pygame.font.SysFont(None, 30)
    reloj = pygame.time.Clock()

    puntaje = 0
    tiempo_juego = 30   # 30 segundos
    tiempo_inicio = time.time()
    
    objetivo_radio = 30
    objetivo_pos = [random.randint(50, 550), random.randint(50, 350)] #Sirve para que los objetivos no aparezcan pegados all borde de la pantalla y de manera aleatoria
    
    
    corriendo = True
    while corriendo==True:
        pantalla.fill((30, 30, 30))
        
        pygame.draw.circle(pantalla, (255, 0, 0), objetivo_pos, objetivo_radio) #Dibuja el circulo
        
        tiempo_restante = tiempo_juego - (time.time() - tiempo_inicio) #Calcular el tiempo
        if tiempo_restante <= 0:
            corriendo = False
            pygame.quit()
            messagebox.showinfo("¡Fin del Juego!",f"{nombre}, tu puntaje fue de {puntaje}")
            actualizar_ranking("🎯ClickTheTarget",nombre,puntaje)
            mostrar_ranking("🎯ClickTheTarget")
            break
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                tk.Tk().withdraw()
                messagebox.showinfo("Juego cerrado",f"{nombre}, saliste del juego")
                return
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                dx = mx - objetivo_pos[0]
                dy = my - objetivo_pos[1]
                if dx * dx + dy * dy <= objetivo_radio * objetivo_radio:
                    puntaje += 1
                    objetivo_pos = [random.randint(50, 550), random.randint(50, 350)]
        
        texto_tiempo = fuente.render(f"Tiempo: {"{:.1f}".format(tiempo_restante)}", True, (255, 255, 255))
        pantalla.blit(texto_tiempo, (450, 10))
        texto_puntaje = fuente.render(f"Puntos: {puntaje}", True, (255, 255, 255))
        pantalla.blit(texto_puntaje, (20, 10))
        pygame.display.flip()
        
        
        
        reloj.tick(60)

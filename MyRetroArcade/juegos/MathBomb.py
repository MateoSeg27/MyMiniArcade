import pygame
import random
import tkinter as tk
from tkinter import messagebox
from ranking.ranking_manager import actualizar_ranking,mostrar_ranking


def generar_pregunta():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    resultado = a + b
    opciones = [resultado, resultado + random.randint(1, 3), resultado - random.randint(1, 3)]
    random.shuffle(opciones)
    return f"{a} + {b}", resultado, opciones

def jugar(nombre):
    pygame.init()
    pantalla = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("🔢Math Bomb")
    fuente = pygame.font.SysFont(None, 48)
    reloj = pygame.time.Clock()

    puntaje = 0
    tiempo_por_pregunta = 5000  # 5 segundos por pregunta
    corriendo = True

    while corriendo:
        pregunta, correcta, opciones = generar_pregunta()
        start_time = pygame.time.get_ticks()

        botones = []
        pantalla.fill((0, 0, 0))
        texto = fuente.render(pregunta, True, (255, 255, 255))
        pantalla.blit(texto, (250, 50))

        for i, opcion in enumerate(opciones):
            rect = pygame.Rect(200, 150 + i * 70, 200, 50)
            botones.append((rect, opcion))
            pygame.draw.rect(pantalla, (100, 100, 255), rect)
            texto_opcion = fuente.render(str(opcion), True, (255, 255, 255))
            pantalla.blit(texto_opcion, (rect.x + 70, rect.y + 5))

        pygame.display.flip()

        respondido = False
        while not respondido:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - start_time > tiempo_por_pregunta:
                pygame.quit()
                messagebox.showinfo("Juego cerrado",f"{nombre}, saliste del juego")
                corriendo = False  # tiempo agotado
                actualizar_ranking("🔢MathBomb",nombre,puntaje)
                mostrar_ranking("🔢MathBomb")
                break
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                    respondido = True
                    pygame.quit()
                    messagebox.showinfo("¡Haz cerrado el juego!. No hay puntaje")
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for rect, valor in botones:
                        if rect.collidepoint(pos):
                            if valor == correcta:
                                puntaje += 1
                                respondido = True  #Acerto
                            else:
                                corriendo = False  # falló
                                respondido = True
                                pygame.quit()
                                messagebox.showinfo("¡Fin del Juego!",f"{nombre} tu puntaje fue de : {puntaje}")
                                actualizar_ranking("🔢MathBomb", nombre,puntaje)
                                mostrar_ranking("🔢MathBomb")
                                
            reloj.tick(60)

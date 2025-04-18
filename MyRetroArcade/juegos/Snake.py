import pygame
import random
from tkinter import messagebox
from ranking.ranking_manager import actualizar_ranking, mostrar_ranking

def generar_comida(tamaño_celda, ALTO, ANCHO, serpiente):
    while True:
        nueva_comida = [
            random.randint(0, (ANCHO - tamaño_celda) // tamaño_celda) * tamaño_celda,
            random.randint(0, (ALTO - tamaño_celda) // tamaño_celda) * tamaño_celda
        ]
        if nueva_comida not in serpiente:
            return nueva_comida

def jugar(nombre):
    pygame.init()
    ALTO, ANCHO = 600, 600
    color_rojo = (255, 0, 0)
    color_negro = (0, 0, 0)
    color_verde = (0, 255, 0)

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("🐍SNAKE")
    fuente = pygame.font.SysFont(None, 36)
    clock = pygame.time.Clock()

    tamaño_celda = 50
    serpiente = [[100, 100]]
    direccion = (1, 0)
    comida = generar_comida(tamaño_celda, ALTO, ANCHO, serpiente)
    puntaje = 0

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
                pygame.quit()
                messagebox.showinfo("Juego cerrado", f"{nombre}, saliste del juego")
                return
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direccion != (0, 1):
                    direccion = (0, -1)
                elif evento.key == pygame.K_DOWN and direccion != (0, -1):
                    direccion = (0, 1)
                elif evento.key == pygame.K_LEFT and direccion != (1, 0):
                    direccion = (-1, 0)
                elif evento.key == pygame.K_RIGHT and direccion != (-1, 0):
                    direccion = (1, 0)

        nueva_cabeza = [serpiente[0][0] + direccion[0] * tamaño_celda,
                        serpiente[0][1] + direccion[1] * tamaño_celda]
        serpiente.insert(0, nueva_cabeza)

        if serpiente[0] == comida:
            puntaje += 1
            comida = generar_comida(tamaño_celda, ALTO, ANCHO, serpiente)
        else:
            serpiente.pop()

        if (serpiente[0] in serpiente[1:] or
            serpiente[0][0] < 0 or serpiente[0][0] >= ANCHO or
            serpiente[0][1] < 0 or serpiente[0][1] >= ALTO):
            corriendo = False
            pygame.quit()
            messagebox.showinfo("¡Fin del Juego!", f"{nombre}, tu puntaje fue de {puntaje}")
            actualizar_ranking("🐍Snake", nombre, puntaje)
            mostrar_ranking("🐍Snake")

        ventana.fill(color_negro)
        pygame.draw.rect(ventana, color_rojo, (*comida, tamaño_celda, tamaño_celda))
        for segmento in serpiente:
            pygame.draw.rect(ventana, color_verde, (*segmento, tamaño_celda, tamaño_celda))

        texto = fuente.render(f"Puntos: {puntaje}", True, (255, 255, 255))
        ventana.blit(texto, (10, 10))
        pygame.display.flip()
        clock.tick(5)

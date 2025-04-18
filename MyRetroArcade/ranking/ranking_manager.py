import os
import tkinter as tk
from tkinter import messagebox

def actualizar_ranking(nombre_juego, jugador, puntaje):
    ruta_archivo = f"ranking/{nombre_juego}_ranking.txt"
    
    if not os.path.exists("ranking"):
        os.makedirs("ranking")

    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, "w") as f:
            pass

    ranking = []
    with open(ruta_archivo, "r") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                nombre, puntos = partes
                ranking.append((nombre, int(puntos)))

    ranking.append((jugador, puntaje))
    ranking.sort(key=lambda x: x[1], reverse=True)
    ranking = ranking[:5]

    with open(ruta_archivo, "w") as f:
        for nombre, puntos in ranking:
            f.write(f"{nombre},{puntos}\n")


def mostrar_ranking(nombre_juego):
    ruta_archivo = f"ranking/{nombre_juego}_ranking.txt"
    if not os.path.exists(ruta_archivo):
        tk.Tk().withdraw()
        messagebox.showinfo("Ranking", "Aún no hay datos guardados para este juego.")
        return

    mensaje = f"🏆 Ranking de {nombre_juego.replace('_', ' ').title()}:\n\n"
    with open(ruta_archivo, "r") as f:
        for i, linea in enumerate(f, start=1):
            partes = linea.strip().split(",")
            if len(partes) == 2:
                nombre, puntos = partes
                mensaje += f"{i}. {nombre} - {puntos} puntos\n"

    tk.Tk().withdraw()
    messagebox.showinfo("Ranking", mensaje)

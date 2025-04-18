import tkinter as tk
from tkinter import *
from utils.PantallaNombre import pedir_nombre
from juegos import (ClickTheTarget, Snake , MathBomb) 


def main():
    name = pedir_nombre()
    if not name:
        return

    ventana=tk.Tk()
    ventana.title("MyRetroArcade")
    ventana.iconbitmap("IITA\MyRetroArcade\Icono.ico")  
    ventana.configure(cursor="right_ptr")
    ventana.resizable(0,0) #1 permisos para cambiar tamaño, 0 si no
    ventana.geometry("600x500")#Tamaño de pantalla
    ventana.config(bg="#000000",) #Usar escala hexadecimal se pueden buscar bordes y cursores que se pueden cambiar aca


    Label1=Label(ventana, text="Selecciona un juego",fg="#fe019a",bg="#000000",font=("Fixedsys", 30,"bold")) #Sirve para poner el texto de seleccionar juego y centrarlo
    Label1.pack(pady=10)
    tk.Button(ventana, text="🎯 ClickeTheTarget",font=("Fixedsys", 15,"bold") ,fg="#B2FFFF",bg="#000000",command=lambda: ClickTheTarget.jugar(name)).pack(pady=5)
    tk.Button(ventana, text= "🐍 Snake", font=("Fixedsys", 15,"bold") ,fg="#B2FFFF",bg="#000000", command=lambda: Snake.jugar(name)).pack(pady=5)
    tk.Button(ventana, text="🔢Math Bomb", font=("Fixedsys", 15,"bold") ,fg="#B2FFFF",bg="#000000", command=lambda : MathBomb.jugar(name)).pack(pady=5)
    ventana.mainloop()

main()
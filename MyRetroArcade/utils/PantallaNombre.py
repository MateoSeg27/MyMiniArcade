import tkinter as tk

def pedir_nombre():
    nombre_usuario=""

    def guardar():
        nonlocal nombre_usuario
        nombre_usuario=entrada.get()
        ventana.destroy()
        
    ventana=tk.Tk()
    ventana.title("ingresar nombre")
    ventana.geometry("400x200")
    ventana.config(bg="#000000")
    ventana.iconbitmap("IITA\MyRetroArcade\Icono.ico") 
    tk.Label(ventana,text="INGRESA TU NOMBRE",fg="#fe019a",bg="#000000",font=("Fixedsys", 30,"bold")).pack(pady=10)

    entrada=tk.Entry(ventana)
    entrada.pack(pady=5)

    button=tk.Button(ventana,text="ACEPTAR",command=guardar,fg="#B2FFFF",bg="#000000",font=("Fixedsys",20,"bold"))
    button.pack(pady=10)

    ventana.mainloop()
    return nombre_usuario

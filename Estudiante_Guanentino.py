#---------------------------------
# Desktop app  datos estudiante
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

# abrir toplevel datos
def datos_salud():
    pass
def datos_estudiante():
    pass
def abrir_toplevel_datos():
    global toplevel_datos
    toplevel_datos = Toplevel()
    toplevel_datos.title("datos")
    toplevel_datos.resizable(False, False)
    toplevel_datos.geometry("300x200")
    toplevel_datos.config(bg="purple")

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Estudiantes Colegio San Jose de Guanentá")

# tamaño de la ventana
ventana_principal.geometry("600x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=580, height=580)
frame_entrada.place(x=10, y=10)


# creamos los objetos para cada imagen
img_datos_estudiante = PhotoImage(file="img/datos_estudiante.png")
img_datos_salud = PhotoImage(file="img/datos_salud.png")

waos = Label (frame_entrada, text="Datos del Estudiante")
waos.config(font=("Arial", 20))
waos.place(x=120, y=10)

# logo de la app
logo = PhotoImage(file ="img/Escudo Colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=15,y=10)

# caja de texto para valor en centigrados
entry_Nombre = Entry(frame_entrada, textvariable="Nombre")
entry_Nombre.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_Nombre.focus_set()
entry_Nombre.place(x=180,y=200)

waos2 = Label (frame_entrada, text="Nombre:")
waos2.config(font=("Arial", 20))
waos2.place(x=60, y=200)

# boton para escojer piedra

bt_datos_estudiante = Button(frame_entrada,image=img_datos_estudiante, command=datos_estudiante)
bt_datos_estudiante.place(x=400, y=100, width=140, height=140)

# boton para escojer papel
bt_papel = Button(frame_entrada, image=img_datos_salud, command=datos_salud)
bt_papel.place(x=400, y=330, width=140, height=140)

ventana_principal.mainloop()

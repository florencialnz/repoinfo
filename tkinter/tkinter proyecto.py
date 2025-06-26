import tkinter as tk

ventana = tk.Tk()
ventana.title("Menu desplegable")
ventana.geometry("400x200")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Principal", menu=menu_principal)

submenu = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Opciones", menu=submenu)


ventana.mainloop()

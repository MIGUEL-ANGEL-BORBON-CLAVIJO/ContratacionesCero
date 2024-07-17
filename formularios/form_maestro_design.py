import tkinter as tk
from tkinter import font
from  config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL,COLOR_CUERPO_PRINCIPAL,COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_imagenes

class FormularioMaestroDesgn(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util_imagenes.lee_imagen("./imagenes/sena.jpg.", (560, 136))
        self.perfil = util_imagenes.lee_imagen("./imagenes/perfil.png.", (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()

    def config_window(self):
        self.title("Contrataciones CENIGRAF")
        self.iconbitmap("./imagenes/sena.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)
        self.labelTitulo = tk.Label(self.barra_superior, text="CENIGRAF")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=13
        )
        self.labelTitulo.pack(side=tk.LEFT)
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome, 
            bd=0,bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)
        
        self.labelTitulo = tk.Label(
            self.barra_superior, text="correo@gmail.com")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family="FontAweson", size=15)
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)
        self.buttonDashBoard = tk.Button(self.menu_lateral)
        self.buttonRegistro = tk.Button(self.menu_lateral)
        self.buttonMovimientos = tk.Button(self.menu_lateral)
        self.buttonBusqueda = tk.Button(self.menu_lateral)
        self.buttonAyuda = tk.Button(self.menu_lateral)
        buttons_info = [
            ("Dashboard","\uf109",self.buttonDashBoard)
            ("Registro","\uf007",self.buttonDashBoard)
            ("Movimientos","\uf03e",self.buttonDashBoard)
            ("Busqueda","\uf129",self.buttonDashBoard)
            ("Ayuda","\uf013",self.buttonDashBoard)
        ]
        for text, icon, button in buttons_info:
            self.configurar_buton_menu(button, text,icon, font_awesome, ancho_menu, alto_menu) 
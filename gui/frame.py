# gui/frame.py

import tkinter as tk
from PIL import Image, ImageTk
from core.game import Game
from math import floor
import os, re

from utils.helpers import *

class ChessApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MyChess")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{floor(screen_width*0.8)}x{floor(screen_height*0.8)}") # 4/5eme de la taille de l'écran
        self.show_main_menu()

    def show_main_menu(self):
        # Effacer l'écran actuel et couleur background main menu
        self.clear_screen()
        self.configure(bg = "dark slate gray")

        # Gestion de la grille du menu
        # Configuration des lignes
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Configuration des colonnes
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Texte de Bienvenue
        label = tk.Label(
            self,
            text="MyChessApp",
            font=("Times New Roman", 48, "bold"),
            fg="antique white",
            bg="dark slate gray"
        )
        label.place(relx=0.5, rely=0.3, anchor="center")

        # Récupération des images de menu dans le dictionnaire img_menu
        partial_path = os.path.join(os.getcwd(), "gui/img_menu/")
        self.img_menu = load_img(partial_path, 256, 256)

        # Boutons du menu principal
        btn_solo_mode = tk.Button(
            self, 
            text="Mode Solo",
            command=self.show_solo_mode_menu,
            image = self.img_menu["toque_universitaire.png"]
        )
        btn_versus_mode = tk.Button(
            self,
            text="Mode Versus",
            command=self.show_versus_mode_menu,
            image = self.img_menu["epees_croisees.png"]
        )

        # Placement des boutons sur la dernière ligne (ligne 2)
        btn_solo_mode.grid(row=2, column=0, padx=10, pady=5)
        btn_versus_mode.grid(row=2, column=1, padx=10, pady=5)

    def show_solo_mode_menu(self):
        # Effacer l'écran actuel et couleur background main menu
        self.clear_screen()
        self.configure(bg = "dark slate gray")

        # Gestion de la grille du menu
        # Configuration des lignes
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Configuration des colonnes
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Boutons du menu principal
        btn_jeu_libre = tk.Button(
            self, 
            text="Jeu Libre",
            command=self.launch_free_game_mode,
            width=15,
            height=5
        )
        btn_sandbox = tk.Button(
            self,
            text="Sandbox",
            command=self.launch_sandbox_mode,
            width=15,
            height=5
        )
        btn_analysis = tk.Button(
            self,
            text="Analyse",
            command=self.launch_analysis_mode,
            width=15,
            height=5
        )
        btn_masterclass = tk.Button(
            self,
            text="Masterclass",
            command=self.launch_masterclass_mode,
            width=15,
            height=5
        )
        btn_return_to_main = tk.Button(
            self,
            text="Menu Principal",
            command=self.show_main_menu,
            width=15,
            height=5
        )

        # Placement des boutons sur la dernière ligne (ligne 2)
        btn_jeu_libre.grid(row=0, column=0, padx=10, pady=5)
        btn_sandbox.grid(row=0, column=1, padx=10, pady=5)
        btn_analysis.grid(row=1, column=0, padx=10, pady=5)
        btn_masterclass.grid(row=1, column=1, padx=10, pady=5)
        btn_return_to_main.grid(row=2, column=1, padx=10, pady=5)

    # --- SOLO GAME MODES --- 
    def launch_free_game_mode(self):
        print("Lancement du jeu libre")
        pass

    def launch_sandbox_mode(self):
        print("Lancement de la Sandbox")
        pass

    def launch_analysis_mode(self):
        print("Lancement du mode Analyse")
        pass

    def launch_masterclass_mode(self):
        print("Lancement du mode Masterclass")
        pass

    def show_versus_mode_menu(self):
        print("Lancement du mode Versus")
        pass

    # --- NETTOYAGE ---
    def clear_screen(self):
        # Détruire tous les widgets de la fenêtre
        for widget in self.winfo_children():
            widget.destroy()


    def run(self):
        self.mainloop()


# class BoardFrame(tk.Canvas):
#     def __init__(self, parent):
#         super().__init__(parent, width=400, height=400, bg="red")
#         self.draw_board()

#     def draw_board(self):
#         # Exemple basique de dessin d'une grille
#         for row in range(8):
#             for col in range(8):
#                 frame = tk.Frame(
#                     self.board_frame, 
#                     width=60, 
#                     height=60, 
#                     bg="antique white" if (row + col) % 2 == 0 else "dark slate gray"
#                 )
#                 frame.grid(row=row, column=col)

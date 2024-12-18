# gui/frame.py

import tkinter as tk
from PIL import Image, ImageTk
from core.game import Game
from math import floor
import os, re

# class ChessApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Jeu d'échecs")
#         self.game = Game()  # Logique du jeu
#         self._setup_ui()

#     def _setup_ui(self):
#         # Créez une grille ou autre pour afficher l'échiquier
#         self.board_frame = tk.Frame(self.root)
#         self.board_frame.pack()
#         self._draw_board()
#         # self._draw_piece(Piece,0,1)

#     def _draw_board(self):
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

#     def _draw_piece(self, board, piece, row, col):
#         # Dessine la Pièce piece situé à la case (row,col) sur le Board board 
#         pass

#     def _erase_piece(self, board, row, col):
#         # Efface le contenu de la case (row,col)

#     def update_display(self):
#         pass

#     def run(self):
#         self.root.mainloop()

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
        """
        Faire une fonction load_img(directory_path, img_width, img_height)
        """
        partial_path = os.path.join(os.getcwd(), "gui/img_menu/")
        png_files = [f for f in os.listdir(partial_path) if f.endswith('.png')]
        self.img_menu = {}
        for i in png_files:
            try : cle_img = re.search(r"^(.*)(?=\.png)", i)[0]
            except TypeError : raise ValueError(f"La regex n'a pas trouvé de match pour la string : {i}")

            image_path = os.path.join(partial_path, i)
            print("=>", image_path)
            try : 
                image = Image.open(image_path)
            except FileNotFoundError: raise FileNotFoundError(f"L'image spécifiée : {image_path}, est introuvable")

            # Redimensionner l'image à stocker dans le dictionnaire
            img_menu_width = 256
            img_menu_height = 256
            image = image.resize((img_menu_width, img_menu_height))
            img = ImageTk.PhotoImage(image) # Conversion pour tkinter
            self.img_menu[cle_img] = img

        print("\n")
        print(self.img_menu)

        # Boutons du menu principal
        btn_solo_mode = tk.Button(
            self, 
            text="Mode Solo",
            command=self.show_solo_mode_menu,
            image = self.img_menu["toque_universitaire"]# ,
            # height=5,
            # width=50
        )
        btn_versus_mode = tk.Button(
            self,
            text="Mode Versus",
            command=self.show_versus_mode_menu,
            image = self.img_menu["epees_croisees"]
        )

        # Placement des boutons sur la dernière ligne (ligne 2)
        btn_solo_mode.grid(row=2, column=0, padx=10, pady=5)
        btn_versus_mode.grid(row=2, column=1, padx=10, pady=5)

    def show_solo_mode_menu(self):
        pass

    def show_versus_mode_menu(self):
        pass

    def show_screen(self):
        self.clear_screen()

    def do_stuff(self):
        pass

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

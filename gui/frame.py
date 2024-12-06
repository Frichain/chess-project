# gui/frame.py

import tkinter as tk
from PIL import Image, ImageTk
from core.game import Game

class ChessApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jeu d'échecs")
        self.game = Game()  # Logique du jeu
        self._setup_ui()

    def _setup_ui(self):
        # Créez une grille ou autre pour afficher l'échiquier
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        self._draw_board()
        # self._draw_piece(Piece,0,1)

    def _draw_board(self):
        # Exemple basique de dessin d'une grille
        for row in range(8):
            for col in range(8):
                frame = tk.Frame(
                    self.board_frame, 
                    width=60, 
                    height=60, 
                    bg="antique white" if (row + col) % 2 == 0 else "dark slate gray"
                )
                frame.grid(row=row, column=col)

    def _draw_piece(self, board, piece, row, col):
        # Dessine la Pièce piece situé à la case (row,col) sur le Board board 
        pass

    def _erase_piece(self, board, row, col):
        # Efface le contenu de la case (row,col)

    def update_display(self):
        pass

    def run(self):
        self.root.mainloop()
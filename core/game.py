# core/game.py

from .board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"  # "white" ou "black"

    def make_move(self, start_pos, end_pos):
        # Implémentez la logique de déplacement des pièces
        pass

    def is_checkmate(self):
        # Vérifie si un roi est en échec et mat
        pass
# core/board.py

from .pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.grid = self._initialize_board()

    def _initialize_board(self):
        # Cases de l'échiquier
        grid = [[None for _ in range(8)] for _ in range(8)]
        # Placement des Pions
        for col in range(8):
            grid[1][col] = Pawn("white")
            grid[6][col] = Pawn("black")
        # Placement des Pièces
        # Tours
        grid[0][0] = Rook("black")
        grid[0][7] = Rook("black")
        grid[7][0] = Rook("white")
        grid[7][7] = Rook("white")
        # Cavaliers
        grid[0][1] = Knight("black")
        grid[0][6] = Knight("black")
        grid[7][1] = Knight("white")
        grid[7][6] = Knight("white")
        # Fous
        grid[0][2] = Bishop("black")
        grid[0][5] = Bishop("black")
        grid[7][2] = Bishop("white")
        grid[7][5] = Bishop("white")
        # Reine et Roi
        grid[0][3] = Queen("black")
        grid[0][4] = King("black")
        grid[7][3] = Queen("white")
        grid[7][4] = King("white")
        return grid

    def get_piece(self, position):
        row, col = position
        return self.grid[row][col]

    def move_piece(self, start_pos, end_pos):
        # Déplace une pièce et met à jour la grille
        piece = get_piece(self, start_pos)
        if piece == None or not piece.is_valid_move(start_pos,end_pos,self.grid) :
            pass

        start_row, start_col = start_pos
        self.grid[start_row][start_col] = None 
        end_row, end_col = end_pos
        self.grid[end_row][end_col] = piece
        pass

    def highlight_square(self, position):
        pass
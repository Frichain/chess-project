# core/pieces.py

class Piece:
    def __init__(self, color):
        self.color = color  # "white" ou "black"

    def is_valid_moves(self, start, end, grid):
        """
        Vérifie si le déplacement est valide
        - start : couple (line,column) position départ
        - end : couple (line,column) position arrivée
        - grid : tableau représentant l'échiquier, None si case vide, autre si case pleine
        Il faut checker que end vaut None mais aussi que toutes les cases intermédiaires entre 
        start et end sont vides (pour pieces long range)
        """
        raise NotImplementedError("Cette méthode doit être implémentée dans les sous-classes.")
        # permet de lever une erreur si is_valid_move n'est pas défini dans une sous classe de pièce
        return []

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)  # Appelle le constructeur de Piece
        # super() récupère les attributs de la classe parent

    def is_valid_move(self, start, end, grid):
        """
        Voir description dans classe Piece
        """

        start_row, start_col = start
        end_row, end_col = end
        direction = -1 if self.color == 'white' else 1 # le tableau est indexé de gauche à droite et de bas en haut

        # Vérification du déplacement de base (une case vers l'avant)
        if (end_row == start_row + 1*direction) and (start_col == end_col) and (grid[end_row][end_col] == None):
            return True

        return False

    pass

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)  # Appelle le constructeur de Piece

    def is_valid_move(self, start, end, grid):
        """
        Voir description dans classe Piece
        """
        return True
    pass

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)  # Appelle le constructeur de Piece

    def is_valid_move(self, start, end, grid):
        """
        Voir description dans classe Piece
        """
        return True
    pass

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)  # Appelle le constructeur de Piece

    def is_valid_move(self, start, end, grid):
        """
        Voir description dans classe Piece
        """
        return True
    pass

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)  # Appelle le constructeur de Piece

    def is_valid_move(self, start, end, grid):
        """
        Voir description dans classe Piece
        """
        return True
    pass

class King(Piece):
    def __init__(self, color):
        super().__init__(color)  # Appelle le constructeur de Piece

    def is_valid_move(self, start, end, grid):
        """
        Voir description dans classe Piece
        """
        return True
    pass
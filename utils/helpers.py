# utils/helpers.py

def is_valid_position(position):
    """Vérifie si une position est valide sur l'échiquier."""
    row, col = position
    return 0 <= row < 8 and 0 <= col < 8

def position_to_chess_notation(position):
    """Convertit une position (ligne, colonne) en notation échiquéenne."""
    row, col = position
    return f"{chr(col + 97)}{8 - row}"

def chess_notation_to_position(notation):
    """Convertit une notation échiquéenne en position (ligne, colonne)."""
    col = ord(notation[0]) - 97
    row = 8 - int(notation[1])
    return (row, col)
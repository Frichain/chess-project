# utils/helpers.py

from PIL import Image, ImageTk
import os

def load_img(dir_path, img_width, img_height):
    images = {}
    for file_name in os.listdir(dir_path):
        if file_name.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            file_path = os.path.join(dir_path, file_name)
            image = Image.open(file_path).resize((img_width, img_height))
            images[file_name] = ImageTk.PhotoImage(image)
    return images

# def is_valid_position(position):
#     """Vérifie si une position est valide sur l'échiquier."""
#     row, col = position
#     return 0 <= row < 8 and 0 <= col < 8

# def position_to_chess_notation(position):
#     """Convertit une position (ligne, colonne) en notation échiquéenne."""
#     row, col = position
#     return f"{chr(col + 97)}{8 - row}"

# def chess_notation_to_position(notation):
#     """Convertit une notation échiquéenne en position (ligne, colonne)."""
#     col = ord(notation[0]) - 97
#     row = 8 - int(notation[1])
#     return (row, col)
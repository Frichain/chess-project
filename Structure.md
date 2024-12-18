# À LIRE
Notes d'avant dodo pour la prochaine session : 
- J'ai peut-être tout fait à l'envers, c'est l'interface graphique qui envoit des infos aux classes CORE donc on doit exécuter les fonctions de core dans gui
- Toute la structure de gui est de toute façon à refaire donc se focaliser sur les mouvements des pieces en premier lieu. Commencer uniquement avec le pion et faire une interface simple pour vérifier que tout marche bien.
- MERDE à toi mon pote




# Structure du code
## 📂 gui
Ce dossier gère tous ce qui concerne l'affichage de l'interface (et uniquement l'affichage). 

Il est très important de faire attention à ne jamais intervenir sur le placement des pièces dans une partie. Seulement l'affichage des éléments.

### 📄 frame.py
**Structure du fichier** : ATTENTION IL Y A PLEIN DE CHOSES A CHANGER NIVEAU INTERFACE, FAIRE LES CORE EN PREMIER, PLUS SIMPLE
- Classes :
    - ``ChessApp`` : Cette classe gère l'affichage général de l'application, 
        - ``__init__(self)`` : Initialisation de la classe, cette méthode exécute la méthode ``_setup_ui()``
        - ``_setup_ui(self)`` : Gère le placement des différentes interfaces utilisateurs à afficher. Crée un canva à gauche pour l'affichage de l'échiquier, et une zone de texte à gauche pour l'écriture du **pgn**
    - ``BoardUI`` :
        - ``__init__(self)`` : Initialisation du canva et récupération du Board (le vrai, pas le UI)
        ```
        def __init(self):
            self.root = tk.des_trucs()
            ...
            self.board = get_board()
        ```
        On a besoin d'avoir la grid du vrai board sinon ... JE SUIS PAS SUR DU TOUT IL EST 3h du mat ==> DODO
        - ``_draw_board(self)`` : Dessine le quadrillage de l'échiquier
        - ``_draw_initial_pos(self)`` : Place les images des pièces en position initiale
        - ``_draw_move(self, board, start, end)`` : Déplace l'image de la piece (si existante) de la position start à la position stop (la vérification de validité du coup est géré dans board.py)
        - ``_draw_promotion(self, board, pion, row, col)`` : Change l'image d'un pion en celle d'une autre piece (pour commencer on fera une promotion en dame automatique)
        - hightlight_square(self, board)
    - TextPGN : _tbd_


## 📂 core
### 📄 board.py
**Structure du fichier** :
- Classes :
    - ``Board`` 
        - ``__init__(self)`` : Initialisation de la classe, appelle la méthode ``_initialize_board()``
        - ``_initialize_board(self)`` : Initialise l'échiquier, un tableau a 2 dimensions contenant :
            - ``None`` si la case est vide
            - un objet ``Piece`` sinon
        - ``get_piece(self, position)`` : Retourne le contenu de la case correspondante à ``position``
        - ``move_piece(self, start_pos, end_pos)`` : Transfère le contenu de la case ``start_pos`` vers la case ``end_pos``
### 📄 pieces.py
**Structure du fichier** :
- Classes :
    - ``Piece`` 
        - ``__init__(self, color)`` : Initialisation de la classe, définit la couleur (blanc ou noir)
        - ``is_valid_moves(self, start, end, grid)`` : Vérifie la validité du déplacement. Cette méthode est définie dans la classe parente pour lever une erreur si jamais une classe fille n'a pas définie cette méthode
    - ``Pawn(Piece)`` : classe fille de ``Piece``
        - ``__init__(self, color)``
        - ``is_valid_moves(self, start, end, grid)`` : Vérifie la validité du déplacement pour cette piece.
    - ``Rook(Piece)`` : classe fille de ``Piece``
        - ``__init__(self, color)``
        - ``is_valid_moves(self, start, end, grid)`` : Vérifie la validité du déplacement pour cette piece.
    - ``Knight(Piece)`` : classe fille de ``Piece``
        - ``__init__(self, color)``
        - ``is_valid_moves(self, start, end, grid)`` : Vérifie la validité du déplacement pour cette piece.
    - ``Bishop(Piece)`` : classe fille de ``Piece``
        - ``__init__(self, color)``
        - ``is_valid_moves(self, start, end, grid)`` : Vérifie la validité du déplacement pour cette piece.
    - ``Queen(Piece)`` : classe fille de ``Piece``
        - ``__init__(self, color)``
        - ``is_valid_moves(self, start, end, grid)`` : Vérifie la validité du déplacement pour cette piece.
    - ``King(Piece)`` : classe fille de ``Piece``
        - ``__init__(self, color)``
        - ``is_valid_moves(self, start, end, grid)`` : Vérifie la validité du déplacement pour cette piece.
## 📂 utils
### 📄 helpers.py
## 📂 main
### 📄 main.py


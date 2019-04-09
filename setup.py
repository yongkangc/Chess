#python 3

""" executable file
Anyone without python can run this 
"""

import cx_Freeze

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("Game.py")]

cx_Freeze.setup(
        name = "Chess",
        options={"build_exe": {"packages":["pygame"],
                           "include_files":["piece.py","Board.py","img/white_rook.png",
"img/bg.png","img/black_bishop.png","img/black_king.png","img/black_knight.png","img/black_pawn.png","img/black_queen.png","img/black_rook.png","img/board.png","img/board_alt.png",
"img/numbers.png","img/sprites.png","img/text.png","img/white_bishop.png","img/white_king.png","img/white_knight.png","img/white_pawn.png","img/white_queen.png"
]}},
    executables = executables,
    version="1.0.0"

        )
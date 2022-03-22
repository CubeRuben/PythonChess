from chessPiece import ChessPiece
from pawn import Pawn
from color import Color
from point import Point

class Board:

    def __init__(self):
        self.colorTurn = Color.WHITE
        self.field = []
        self.tookedPiece = None
        for _ in range(8):
            self.field.append([None] * 8)

        self.field[2][2] = Pawn(2, 2, Color.BLACK, self)

        for x in range(8):
            self.field[x][1] = Pawn(x, 1, Color.WHITE, self)
            self.field[x][6] = Pawn(x, 6, Color.BLACK, self)

    def draw(self):
        print("   /--" + "--+--" * 7 + "--\\")

        for y in range(7, -1, -1):

            if y != 7:
                print("   +--" + "--+--" * 7 + "--+")
            
            print(f" {y + 1} ", end="")

            for x in range(8):
                cell = "|"

                if self.tookedPiece == None:
                    if self.field[x][y] == None:
                        cell += "    "
                    else:
                        cell += f" {self.field[x][y]} "
                else:
                    if self.field[self.tookedPiece.x][self.tookedPiece.y].can_move(x, y):
                        if self.field[x][y] == None:
                            cell += " <> "
                        else:
                            cell += f">{self.field[x][y]}<"
                    else:
                        if self.field[x][y] == None:
                            cell += "    "
                        else:
                            if x == self.tookedPiece.x and y == self.tookedPiece.y:
                                cell += f"*{self.field[x][y]}*"
                            else:
                                cell += f" {self.field[x][y]} "

                print(cell, end="")
            
            print("|")

        print("   \--" + "--+--" * 7 + "--/")
        print("   ", end="")
        for i in range(8):
            print(f"  {chr(ord('A') + i)}  ", end="")
        print()

    def move_tooked_piece(self, coords):
        point = Point(coords)

        if not point.is_in_range(8, 8):
            return "Выбранная клетка за пределами доски"


    def took_chess_piece(self, coords):
        point = Point(coords)
        
        if not point.is_in_range(8, 8):
            return "Выбранная клетка за пределами доски"
        
        if self.cell_is_free(point.x, point.y):
            return "На выбранной клетке нет фигуры"

        if self.get_piece(point.x, point.y).get_color() != self.colorTurn:
            return "Это фигура опонента"

        self.tookedPiece = point
        return "Фигура взята"

    def get_piece(self, x, y):
        return self.field[x][y]

    def cell_is_free(self, x, y):
        return self.get_piece(x, y) == None

    def is_oponent_on_cell(self, x, y, piece):
        if self.cell_is_free(x, y):
            return False
        
        if piece.is_oponent(self.get_piece(x, y)):
            return True

        return False

    def is_friend_on_cell(self, x, y, piece):
        if self.cell_is_free(x, y):
            return False
        
        if piece.is_friend(self.get_piece(x, y)):
            return True

        return False

    def piece_is_tooked(self):
        return self.tookedPiece == None

def main():
    board = Board()
    
    board.draw()

    while True:

        args = input().split(' ')

        if args[0] == "took":
            print(board.took_chess_piece(args[1]))
        elif args[0] == "move":
            print(board.move_tooked_piece(args[1]))

        board.draw()

main()
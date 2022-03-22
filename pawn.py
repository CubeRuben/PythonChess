from msilib.schema import tables
from operator import truediv
from chessPiece import ChessPiece
from color import Color

class Pawn(ChessPiece):

    def get_char(self):
        return "P"

    def can_move(self, x, y):
        delta = 1

        if self.color == Color.BLACK:
            delta = -1

        if self.table.is_friend_on_cell(x, y, self):
            return False

        if x == self.x and self.table.cell_is_free(self.x, self.y + delta):
            if y == self.y + delta:
                return True

            if self.y in [1, 6] and y == (self.y + delta * 2):
                return True
        elif x in [self.x - 1, self.x + 1]:
            if y == self.y + delta:
                if self.table.is_oponent_on_cell(x, y, self):
                    return True
        

        return False
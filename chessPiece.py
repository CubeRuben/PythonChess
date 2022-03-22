
class ChessPiece:

    def __init__(self, x, y, color, table):
        self.x = x
        self.y = y
        self.color = color
        self.table = table
        
    def get_char(self):
        return "0"
    
    def get_color(self):
        return self.color

    def is_oponent(self, piece):
        return not self.is_friend(piece)

    def is_friend(self, piece):
        return self.color == piece.get_color()

    def __str__(self):
        return self.color.name.lower()[0] + self.get_char()

    def can_move(self, x, y):
        return True

    def move(self, x, y):
        pass
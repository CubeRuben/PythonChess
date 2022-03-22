class Point:

    def __init__(self, coords):
        self.x = ord(coords[0].lower()) - ord('a')
        self.y = int(coords[1]) - 1

    def is_in_range(self, x, y):
        return (self.x in range(x)) and (self.y in range(y))
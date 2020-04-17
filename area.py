from colour import Color


class Area:
    """
    This is an Abstract Class. Price() method should be implemented.
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def price(self):
        raise NotImplementedError(f"Class {self.__class__.__name__} doesn't implement price()")


class ParquetFloor(Area):

    def price(self):
        return int(self.width) * int(self.height) * int(Color(self.color).hex.replace('#', ''), 16) * 5


class WoodenFloor(Area):

    def price(self):
        return int(self.width) * int(self.height) * int(Color(self.color).hex.replace('#', ''), 16) * 3

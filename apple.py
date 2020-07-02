from circle import *

class Apple:
    def __init__(self):
        self.position = Vector2(30, 60)
        self.radious = 15
        self.circle = Circle(self.position, self.radious)
        self.circle.setColor(255, 0, 0)

    def draw(self, window):
        self.circle.draw(window)

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position
        self.circle.setPosition(position)
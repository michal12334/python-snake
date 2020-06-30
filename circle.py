import pygame
from vector2 import *

class Circle:
    def __init__(self, position = Vector2(0, 0), radious = 0):
        self.setPosition(position)
        self.setRadious(radious)
        self.color = 255, 255, 255

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def setRadious(self, radious):
        self.radious = radious

    def getRadious(self):
        return self.radious

    def setColor(self, r, g, b):
        self.color = r, g, b

    def getColor(self):
        return self.color

    def draw(self, window):
        pygame.draw.circle(window.getPygameSurface(), self.color, (self.position.x + self.radious, self.position.y + self.radious), self.radious)
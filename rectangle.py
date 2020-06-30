from vector2 import *
import pygame

class Rectangle:
    def __init__(self, position = Vector2(0, 0), size = Vector2(0, 0)):
        self.setPosition(position)
        self.setSize(size)
        self.color = 255, 255, 255

    def setPosition(self, position):
        self.position = position

    def setSize(self, size):
        self.size = size

    def getPosition(self):
        return self.position

    def getSize(self):
        return self.size

    def setColor(self, r, g, b):
        self.color = r, g, b

    def getColor(self):
        return self.color

    def draw(self, window):
        pygame.draw.rect(window.getPygameSurface(), self.color, (self.position.x, self.position.y, self.size.x, self.size.y))

import pygame

class Window:
    def __init__(self, width = 300, height = 300):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def draw(self, obj):
        obj.draw(self)

    def setFrameRateLimit(self, fps):
        self.fps = fps

    def setTitle(self, title):
        pygame.display.set_caption(title)

    def display(self):
        pygame.display.update()

    def getPygameSurface(self):
        return self.window

    def clear(self, color = (0, 0, 0)):
        self.window.fill(color)
        self.clock.tick(self.fps)
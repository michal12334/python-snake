import pygame
from window import *
from snake import *
from apple import *

def gameLoop():
    snake.update()

    if snake.isAppleEaten(apple.getPosition()):
        apple.setPosition(snake.generateNewPositionForApple())
        snake.addNewPart()

    window.draw(snake)
    window.draw(apple)

def main():
    window = Window(900, 900)
    window.setTitle("Snake")
    window.setFrameRateLimit(60)

    isOpen = True

    snake = Snake()

    apple = Apple()

    while isOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isOpen = False

        window.clear()
        gameLoop()    
        window.display()

main()
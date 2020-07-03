import pygame
from window import *
from snake import *
from apple import *

pygame.font.init()

def showYouLost(window):
    font = pygame.font.SysFont("comicsans", 60)
    text = font.render("You lost", 1, (255, 255, 255))
    window.blit(text, (420, 200))

def main():
    window = Window(900, 900)
    window.setTitle("Snake")
    window.setFrameRateLimit(60)

    isOpen = True

    snake = Snake()

    apple = Apple()

    isDead = False
    counter = 0
    counterMax = 3 * 60

    while isOpen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isOpen = False

        if snake.isAppleEaten(apple.getPosition()):
            apple.setPosition(snake.generateNewPositionForApple())
            snake.addNewPart()

        snake.update()

        window.clear()

        if not isDead:
            window.draw(snake)
            window.draw(apple)
            isDead = snake.isDead()
        else:
            counter += 1
            if counter >= counterMax:
                isOpen = False
            showYouLost(window.getPygameSurface())
        window.display()

main()
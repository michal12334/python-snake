from rectangle import *
import time
import random

# Direction:
UP = 1
BOTTOM = 2
RIGHT = 3
LEFT = 4

class Snake:
    SNAKE_PART_SIZE = Vector2(30, 30)

    def __init__(self):
        self.snakeParts = [Rectangle(Vector2(300, 300), self.SNAKE_PART_SIZE), Rectangle(Vector2(300, 330), self.SNAKE_PART_SIZE)]
        self.snakeParts[0].setColor(0, 255, 0)
        self.snakeParts[1].setColor(0, 255, 0)
        self.direction = UP
        self.newDirection = UP
        self.counter = 0
        self.counterTime = 12

    def draw(self, window):
        for part in self.snakeParts:
            part.draw(window)

    def isUpButtonClicked(self, keys):
        return keys[pygame.K_w] or keys[pygame.K_UP]

    def isBottomButtonClicked(self, keys):
        return keys[pygame.K_s] or keys[pygame.K_DOWN]

    def isRightButtonClicked(self, keys):
        return keys[pygame.K_d] or keys[pygame.K_RIGHT]

    def isLeftButtonClicked(self, keys):
        return keys[pygame.K_a] or keys[pygame.K_LEFT]

    def setNewDirection(self):
        keys = pygame.key.get_pressed()

        if self.isUpButtonClicked(keys) and self.direction != BOTTOM:
            self.newDirection = UP
        elif self.isBottomButtonClicked(keys) and self.direction != UP:
            self.newDirection = BOTTOM
        elif self.isRightButtonClicked(keys) and self.direction != LEFT:
            self.newDirection = RIGHT
        elif self.isLeftButtonClicked(keys) and self.direction != RIGHT:
            self.newDirection = LEFT

    def setAllPartsPosition(self):
        for i in range(len(self.snakeParts) - 1, 0, -1):
            self.snakeParts[i].setPosition(self.snakeParts[i - 1].getPosition())
        
        x = self.snakeParts[0].getPosition().x
        y = self.snakeParts[0].getPosition().y
        if self.direction == UP:
            self.snakeParts[0].setPosition(Vector2(x, y - 30))
        elif self.direction == BOTTOM:
            self.snakeParts[0].setPosition(Vector2(x, y + 30))
        elif self.direction == RIGHT:
            self.snakeParts[0].setPosition(Vector2(x + 30, y))
        else:
            self.snakeParts[0].setPosition(Vector2(x - 30, y))


    def update(self):
        self.setNewDirection()

        self.counter += 1

        if(self.counter >= self.counterTime):
            self.counter = 0
            self.direction = self.newDirection
            self.setAllPartsPosition()

    def isAppleEaten(self, position):
        for snakePart in self.snakeParts:
            if snakePart.getPosition().x == position.x and snakePart.getPosition().y == position.y:
                return True
        return False

    def generateNewPositionForApple(self):
        position = Vector2(random.randrange(0, 29) * 30, random.randrange(0, 29) * 30)
        while self.isAppleEaten(position):
            position = Vector2(random.randrange(0, 29) * 30, random.randrange(0, 29) * 30)
        return position

    def addNewPart(self):
        newPart = Rectangle(self.snakeParts[len(self.snakeParts) - 1].getPosition(), self.SNAKE_PART_SIZE)
        newPart.setColor(0, 255, 0)
        self.snakeParts.append(newPart)

    def isHitItself(self):
        x = self.snakeParts[0].getPosition().x
        y = self.snakeParts[0].getPosition().y
        for i in range(1, len(self.snakeParts)):
            xn = self.snakeParts[i].getPosition().x
            yn = self.snakeParts[i].getPosition().y
            if xn == x and yn == y:
                return True
        return False

    def isHitWall(self):
        x = self.snakeParts[0].getPosition().x
        y = self.snakeParts[0].getPosition().y
        return x < 0 or x + self.SNAKE_PART_SIZE.x > 900 or y < 0 or y + self.SNAKE_PART_SIZE.y > 900

    def isDead(self):
        return self.isHitItself() or self.isHitWall()
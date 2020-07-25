import pygame

class ball():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (255, 255, 255)
        self.side = 1
        self.end = 1
        self.Rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def move(self):
        self.x += 2 * self.side
        self.y += 2 * self.end

    def collide_check(self, b1, b2):
        if self.Rect.colliderect(b1):
            print("burger")
            self.lateral_flip()
            self.move()
            self.move()
        elif self.Rect.colliderect(b2):
            self.lateral_flip()
            self.move()
            self.move()

        if self.x == 0 or self.x == 800 - self.size:
            return True
        if self.y == 0 or self.y == 600 - self.size:
            self.vertical_flip()

    def lateral_flip(self):
        if self.side == 1:
            self.side = -1
        else:
            self.side = 1

    def vertical_flip(self):
        if self.end == 1:
            self.end = -1
        else:
            self.end = 1

    def draw(self, win):
        self.Rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.size, self.size))

class board():
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 80
        self.colour = (255, 255, 255)
        self.Rect = (self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == 0 and self.y > 1:
            self.y -= 2
        elif self.y < 600 - self.height - 1:
            self.y += 2

    def draw(self, win):
        self.Rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))